from django.db import models
from django.utils import timezone


class Task(models.Model):
	name = models.CharField(max_length = 100)
	created = models.DateTimeField(default = timezone.now())
	due_on = models.DateTimeField(default = timezone.now())
	owner = models.CharField(max_length = 100)
	status = False

    def create(self):
        self.created = timezone.now()
        self.save()

    def status(self):
    	return self.status

    def __str__(self):
        return self.name