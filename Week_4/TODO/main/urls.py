from django.urls import path
from . import views

urlpatterns = [
	path('', views.task_list, name = 'task_list'),
	path('completed_list/', views.completed_list, name ='completed_list'),
	path('delete_list', views.delete_list, name = 'delete_list'),
	path('completed_list/', views.delete_completed, name = 'delete_completed'),
	path('delete_task/<task_id>', views.delete_task, name = 'delete_task'),
	path('delete_completed_task/<task_id>', views.delete_completed_task, name = 'delete_completed_task'),
	path('add_to_completed/<task_id>', views.add_to_completed, name = 'add_to_completed'),
]