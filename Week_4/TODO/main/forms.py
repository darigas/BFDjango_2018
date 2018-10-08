from django import forms
from .models import Task, CompletedTask

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ["name", "created", "due_on"]

class CompletedTaskForm(forms.ModelForm):
	class Meta:
		model = CompletedTask
		fields = ["name", "created", "due_on"]