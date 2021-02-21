from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField('Created', '', auto_now_add=True)
    due_on = models.DateTimeField('Due on')
    owner = models.CharField('Owner', max_length=200)
    done = models.NullBooleanField('Done')

    def __str__(self):
        return self.title
