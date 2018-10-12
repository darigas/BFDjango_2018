from django.urls import path
from . import views

urlpatterns = [
	path('', views.posts_list, name = 'posts_list'),
	path('add_post/', views.add_post, name = 'add_post'),
	path('edit_post/<post_id>', views.edit_post, name = 'edit_post'),
	path('delete_post/<post_id>', views.delete_post, name = 'delete_post'),
	path('home', views.home, name = 'home'),
]