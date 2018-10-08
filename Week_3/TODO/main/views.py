from django.shortcuts import render
from django.http import HttpResponse
import datetime

def todo(request):
	todo = {
		'Tasks' : ['Task 1', 'Task 2', 'Task 3', 'Task 4'],
		'Created' : datetime.datetime.now(),
		'Due' : datetime.datetime.now(),
		'Owner' : "admin",
	}
	return render(request, 'main/todo.html', todo)

def todo_completed(request):
    done = {
		'Tasks' : ['Task 0', 'Task 1'],
		'Created' : datetime.datetime.now(),
		'Due' : datetime.datetime.now(),
		'Owner' : "admin",
    }
    return render(request, 'main/completed_todo_list.html',done)


