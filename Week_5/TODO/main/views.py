from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.utils import timezone
from django.contrib import messages
from .forms import TaskForm
from django.http import HttpResponseRedirect

def task_list(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			tasks = Task.objects.filter(mark = False)
			return render(request,'main/task_list.html', {'tasks': tasks})
	else:
		tasks = Task.objects.filter(mark = False)
	return render(request, 'main/task_list.html', {'tasks': tasks})

def completed_task_list(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			tasks = Task.objects.filter(mark = True)
			return render(request,'main/completed_task_list.html', {'tasks': tasks})
	else:
		tasks = Task.objects.filter(mark = True)
	return render(request, 'main/completed_task_list.html', {'tasks': tasks})

def delete_list(request):
	Task.objects.filter(mark = False).delete()
	tasks = Task.objects.all()
	return redirect('task_list')

def delete_completed_list(request):
	Task.objects.filter(mark = True).delete()
	tasks = Task.objects.all()
	return redirect('task_list')

def delete_completed_task(request, task_id):
	item = Task.objects.filter(mark = True).get(pk = task_id)
	item.delete()
	return  redirect('completed_task_list')

def delete_task(request, task_id):
	item = Task.objects.filter(mark = False).get(pk = task_id)
	item.delete()
	return  redirect('task_list')

def add_to_completed(request, task_id):
	Task.objects.filter(mark = False).filter(pk = task_id).update(mark = True)
	return redirect('completed_task_list')

def add_new_task(request):
	task = Task()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		print(form.errors)
		if form.is_valid():
			task.name = form.cleaned_data['name']
			task.created = form.cleaned_data['created']
			task.due_on = form.cleaned_data['due_on']
			task.owner = form.cleaned_data['owner']
			task.save()
			return redirect('task_list')
	else:
		form = TaskForm()
	return render(request, 'main/new_task.html', {'form': form})

def update_task(request, task_id):
	task = Task.objects.get(pk = task_id)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance = task)
		if form.is_valid():
			task.name = form.cleaned_data['name']
			task.created = form.cleaned_data['created']
			task.due_on = form.cleaned_data['due_on']
			task.owner = form.cleaned_data['owner']
			task = form.save(commit = False)
			task.save()
			print(form.errors)
			return redirect('task_list')
	else:
		form = TaskForm(instance =  task)
		return render(request, 'main/update_task.html', {'form' : form})

