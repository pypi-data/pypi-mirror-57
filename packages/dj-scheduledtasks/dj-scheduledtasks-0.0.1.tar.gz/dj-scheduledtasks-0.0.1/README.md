# dj-scheduledtasks

Run tasks at a scheduled time

## Installation

```
pip install ..
```

## Getting started

```python
from scheduledtasks.models import ScheduledTask
```

### Schedule a task:

**Explicit schedule**

```python
# minimal usage
ScheduledTask.schedule('example_project.tasks.remind_if_due')
# minimal usage
ScheduledTask.schedule('remind_if_due')
```

**Schedule from a related object**

You can also schedule infer the scheduled time from an object by passing the object instance, a field and an offset. e.g.:

```python
# run a task 60 minutes after the due date
ScheduledTask.schedule_by_object(
    todo,
    'example_project.tasks.remind_if_due',
    'due_date',
    offset=60
)
```

### Create a task

### Ways to run a task

### Cleanup old tasks
