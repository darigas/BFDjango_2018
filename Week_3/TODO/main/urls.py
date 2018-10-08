from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo, name = 'todo'),
    path('todo/1/completed', views.todo_completed)
]
