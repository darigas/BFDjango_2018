from django.db import models
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length = 100, default = 'Post')
	created = models.DateTimeField(default = timezone.now)
	text = models.TextField()

	def __str__(self):
		return self.title

class Comement(models.Model):
	created = models.DateTimeField(timezone.now)
	user = models.CharField(max_length = 100)
	text = models.TextField()
	comment_id = models.ForeignKey('Post', on_delete = models.CASCADE, related_name = 'comments')