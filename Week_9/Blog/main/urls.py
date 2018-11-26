from .views import HomeView, PostCreate, PostList, PostDelete, PostUpdate, PostDetail, CommentCreate, CommentDelete
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('post/create/', PostCreate.as_view(), name = 'post_create'),
    path('post/list/', PostList.as_view(), name = 'post_list'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name = 'post_delete'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name = 'post_update'),
    path('post/<int:pk>/detail/', PostDetail.as_view(), name = 'post_detail'),
    path('comment/<int:pk>/', CommentCreate.as_view(), name = 'comment_create'),
    path('comment/delete/<int:pk>/', CommentDelete.as_view(), name = 'comment_delete'),
]