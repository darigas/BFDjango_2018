from django.urls import path
from . import views

urlpatterns = [
	path('', views.task_list, name = 'task_list'),
	path('completed_task_list/', views.completed_task_list, name = 'completed_task_list'),
	path('', views.delete_list, name = 'delete_list'),
	path('completed_task_list', views.delete_completed_list, name = 'delete_completed_list'),
	path('delete_task/<task_id>', views.delete_task, name = 'delete_task'),
	path('delete_completed_task/<task_id>', views.delete_completed_task, name = 'delete_completed_task'),
	path('add_to_completed/<task_id>', views.add_to_completed, name = 'add_to_completed'),
	path('new_task/', views.add_new_task, name = 'add_new_task'),
	path('update_task/<task_id>', views.update_task, name = 'update_task'),
]