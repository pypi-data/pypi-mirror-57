from django.contrib import admin

from .models import ScheduledTask, ScheduledTaskRun

class ConditionInline(admin.StackedInline):
    model = ScheduledTaskRun
    extra = 0

class ScheduledTaskAdmin(admin.ModelAdmin):
    # list_display = ('type', 'owner', 'name', 'model_name', 'owner', 'task',)
    # list_filter = ('model_name', 'type', 'task')
    # search_fields = ('owner', 'task')
    inlines = [ConditionInline]

admin.site.register(ScheduledTask, ScheduledTaskAdmin)
