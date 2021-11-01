from django.shortcuts import redirect, render
from .models import Post
from django.views.generic import ListView, DetailView


class Index(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    ordering = ['-date_posted']

class Single(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    ordering = ['-date_posted']


def About(request):
    return render(request, 'blog/about.html')

def Contact(request):
    return render(request, 'blog/contact.html')

def Gallery(request):
    return render(request, 'blog/gallery.html')





