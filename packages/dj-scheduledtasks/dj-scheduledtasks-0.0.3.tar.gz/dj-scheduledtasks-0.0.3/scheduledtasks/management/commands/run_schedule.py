from django.core.management.base import BaseCommand
from scheduledtasks.models import ScheduledTask


class Command(BaseCommand):

    help = 'Run scheduled tasks'

    def handle(self, *args, **options):
        tasks = ScheduledTask.get_scheduled_tasks()
        for task in tasks:
            task.run()