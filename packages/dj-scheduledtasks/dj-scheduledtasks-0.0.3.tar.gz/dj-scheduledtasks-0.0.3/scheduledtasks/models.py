from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.utils.module_loading import import_string
from django.contrib.postgres.fields import ArrayField, JSONField
from datetime import timedelta
from enum import Enum

class STATUS(Enum):
    Scheduled = 'N'
    InProgress = 'IP'
    Success = 'S'
    Failed = 'F'
    TerminallyFailed = 'FX'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

STATUSES = STATUS.choices()

# Create your models here.
class ScheduledTask(models.Model):
    """
    ScheduledTask.
    """

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(default=0, blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    # information required to execute this task
    task = models.CharField(max_length=255, db_index=True, blank=True, null=True, default=None)
    task_id = models.CharField(max_length=255, db_index=True, blank=True, null=True, help_text='You can use this to ensure that duplicate tasks are not created')
    args = ArrayField(
        models.CharField(max_length=255, blank=True),
        blank=True
    )
    kwargs = JSONField(default=dict)
    scheduled_time = models.DateTimeField(db_index=True)
    run_async = models.BooleanField(default=True)

    # fields used for calculating
    offset = models.IntegerField(default=0, null=True, blank=True, db_index=True)
    offset_field = models.CharField(max_length=255, db_index=True, blank=True, null=True, default=None)

    status = models.CharField(max_length=255, db_index=True, default=STATUS.Scheduled)

    # cleanup fields:
    protected = models.BooleanField(default=False, help_text='Protected tasks will not be garbage collected')
    expiry_in_minutes = models.PositiveIntegerField(default=30, help_text='If this many minutes have passed since the scheduled date, this task will be considered terminally failed')
    storage_timeout = models.PositiveIntegerField(default=2880, help_text='Keep this around the many minutes after execution has completed')

    @property
    def calculated_scheduled_time(self):
        reference_field_datetime = getattr(self.content_object, self.offset_field)
        return reference_field_datetime + timedelta(minutes = self.offset)

    @classmethod
    def schedule(cls, task, args=[], kwargs={}, time=None):
        if time is None:
            time = timezone.now()
        scheduled_task = cls()
        scheduled_task.task = task
        scheduled_task.args = args
        scheduled_task.kwargs = kwargs
        scheduled_task.scheduled_time = time
        scheduled_task.save()
        return scheduled_task

    @classmethod
    def schedule_by_object(cls, base_object, task, offset_field, offset=0, args=[], kwargs={}):
        scheduled_task = cls()
        scheduled_task.content_object = base_object
        scheduled_task.task = task
        scheduled_task.args = args
        scheduled_task.kwargs = kwargs
        scheduled_task.offset_field = offset_field
        scheduled_task.offset = offset
        scheduled_task.scheduled_time = scheduled_task.calculated_scheduled_time
        scheduled_task.save()
        return scheduled_task

    @staticmethod
    def get_scheduled_tasks(reference_date=None, window=-60):
        if reference_date is None:
            reference_date = timezone.now()
        window_period = reference_date + timedelta(minutes=window)
        search_in_future = (window > 0)
        if search_in_future:
            return ScheduledTask.objects.filter(
                scheduled_time__gte = reference_date,
                scheduled_time__lte = window_period,
                # status = STATUS.Scheduled.value
            )
        else:
            return ScheduledTask.objects.filter(
                scheduled_time__gte = window_period,
                scheduled_time__lte = reference_date,
                # status = STATUS.Scheduled.value
            )

    def run(self, force = False):
        if force or self.status == STATUS.Scheduled.value:
            self.status = STATUS.InProgress.value
            self.save()
            is_success = True
            try:
                task_to_run = import_string(self.task)
                can_run_async = (getattr(task_to_run, 'delay', None) is not None)
                if can_run_async and self.run_async:
                    result = task_to_run.s(*self.args, **self.kwargs).apply_async()
                else:
                    result = task_to_run(*self.args, **self.kwargs)
                self.status = STATUS.Success.value
            except Exception as e:
                result = str(e)
                is_success = False
                self.status = STATUS.Failed.value
            finally:
                # ideally, maybe do this async?
                self.save()
                ScheduledTaskRun.from_result(self, result, success=is_success)


class ScheduledTaskRun(models.Model):
    """
    The results from running a scheduled task
    """
    task = models.ForeignKey(ScheduledTask, on_delete=models.CASCADE)

    result = models.TextField(blank=True)
    is_success = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @classmethod
    def from_result(cls, task, result ='', success=True):
        run = cls()
        run.task = task
        run.result = result
        run.is_success = success
        run.save()
        return run
