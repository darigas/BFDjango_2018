from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, CompletedTask
from django.utils import timezone
from django.contrib import messages
from .forms import TaskForm, CompletedTaskForm

def task_list(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			tasks = Task.objects.all(mark = False)
			return render(request,'main/task_list.html', {'tasks': tasks})
	else:
		tasks = Task.objects.all()
	return render(request, 'main/task_list.html', {'tasks': tasks})

def completed_list(request):
	if request.method == 'POST':
		form = CompletedTaskForm(request.POST)
		if form.is_valid():
			form.save()
			completedTasks = CompletedTask.objects.all()
			return render(request,'main/сompleted_todo_list.html', {'completedTasks': completedTasks})
	else:
		completedTasks = CompletedTask.objects.all()
	return render(request, 'main/completed_todo_list.html', {'completedTasks': completedTasks})

def delete_list(request):
	Task.objects.all().delete()
	tasks = Task.objects.all()
	return render(request, 'main/task_list.html', {'tasks' : tasks})

def delete_completed(request):
	CompletedTask.objects.all().delete()
	completed = CompletedTask.objects.all()
	return render(request, 'main/completed_todo_list.html', {'completed' : completed})

def delete_task(request, task_id):
	item = Task.objects.get(pk = task_id)
	item.delete()
	return  redirect('task_list')

def delete_completed_task(request, task_id):
	item = CompletedTask.objects.get(pk = task_id)
	item.delete()
	return  redirect('completed_list')

def add_to_completed(request, task_id):
	item = Task.objects.get(pk = task_id)
	item.delete()
	CompletedTask.objects.create(name = item.name, created = item.created, due_on = item.due_on, owner = item.owner, mark = True)
	return redirect('task_list')