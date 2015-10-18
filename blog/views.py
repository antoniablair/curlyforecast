from django.shortcuts import render
from .models import Post
from django.utils import timezone

# . after "from" means current directory

# Method that takes request and returns a method, render, and renders the template
def post_list(request):
		app_title = 'Blog'

		# Queryset for posts that are published
		posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
		return render(request, 'blog/post_list.html', {'posts': posts, 'title': app_title })

