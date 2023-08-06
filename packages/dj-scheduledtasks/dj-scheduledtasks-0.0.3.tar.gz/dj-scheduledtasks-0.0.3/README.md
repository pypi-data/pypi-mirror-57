# dj-scheduledtasks

Run tasks at a scheduled time

[![PyPI version](https://badge.fury.io/py/dj-scheduledtasks.svg)](https://badge.fury.io/py/dj-scheduledtasks)

## Installation

**pip install**

```
pip install dj-scheduledtasks
```

**add to installed apps:**

```python
INSTALLED_APPS = [
    ...
    'scheduledtasks',
]
```

## Getting started

```python
from scheduledtasks.models import ScheduledTask
```

### Adding a reverse lookup to your model

You might want to be able to access the list of scheduled tasks on a model. To make this easy, you can add a `GenericRelation` field

```python
from django.contrib.contenttypes.fields import GenericRelation
from scheduledtasks.models import ScheduledTask

class Todo(models.Model):
    ...
    scheduled_tasks = GenericRelation(ScheduledTask)
```

You can then access `scheduled_tasks_set` just as you would any other `ForeignKey` field

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

.. or just use the model directly

### Create a task

### Ways to run a task

### Cleanup old tasks
