from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, DetailView
from .models import Post, Comment
from django.urls import reverse_lazy
from .forms import PostForm, CommentForm
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    http_method_names = ['get']

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('post_list')
    fields = ['id', 'title', 'created', 'text']

class PostList(ListView):
    model = Post
    context_object_name = 'items'

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_list')
    template_name_suffix = '_update_form'

class PostDetail(DetailView):
    model = Post

class CommentCreate(CreateView):
    model = Comment
    fields = ['comment_id', 'created', 'text']

class CommentDelete(DeleteView):
    model = Comment
    success_url = reverse_lazy('post_list')