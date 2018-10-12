from django.db import models
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length = 100, default = 'Post')
	created = models.DateTimeField(default = timezone.now)
	text = models.TextField()

	def __str__(self):
		return self.title