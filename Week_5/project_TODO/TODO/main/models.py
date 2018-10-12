from django.db import models
from django.utils import timezone

class Task(models.Model):
	name = models.CharField(max_length = 100, default = 'Some task')
	created = models.DateTimeField(default = timezone.now)
	due_on = models.DateTimeField(default = timezone.now() + timezone.timedelta(days = 1))
	owner = models.CharField(max_length = 100, default = 'Admin')
	mark = models.BooleanField(default = False)

	def __str__(self):
		return self.name

	def create(self):
		self.create = timezone.now

	def done(self):
		self.mark = True

