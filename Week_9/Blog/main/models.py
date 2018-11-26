from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default='New Post')
    created = models.DateTimeField(default=timezone.now())
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absoulte_url(self):
        return reverse_lazy('post_list')

class Comment(models.Model):
    comment_id = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments', null=True)
    created = models.DateTimeField(default=timezone.now(), blank=True)
    text = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse_lazy('post_list')