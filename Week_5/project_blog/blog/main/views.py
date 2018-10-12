from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def posts_list(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			posts = Post.objects.all()
			return render(request, 'main/posts_list.html', {'posts' : posts})
	else:
		posts = Post.objects.all()
	return render(request, 'main/posts_list.html', {'posts' : posts})

@login_required
def delete_post(request, post_id):
	item = Post.objects.get(pk = post_id)
	item.delete()
	return redirect('posts_list')

@login_required
def add_post(request):
	post = Post()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post.title = form.cleaned_data['title']
			post.created = form.cleaned_data['created']
			post.text = form.cleaned_data['text']
			post.save()
			return redirect('posts_list')
	else:
		form = PostForm()
	return render(request, 'main/add_post.html', {'form' : form})

@login_required
def edit_post(request, post_id):
	post = Post.objects.get(pk = post_id)
	if request.method == 'POST':
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			post.title = form.cleaned_data['title']
			post.created = form.cleaned_data['created']
			post.text = form.cleaned_data['text']
			post = form.save(commit = False)
			post.save()
			return redirect('posts_list')
	else:
		form = PostForm(instance = post)
		return render(request, 'main/edit_post.html', {'form' : form})

def home(request):
	return render(request, 'main/home.html')

