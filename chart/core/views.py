from multiprocessing import context
from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    
    return render(request, 'index.html', context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'examp.html', context)

def buble(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    
    return render(request, 'buble.html', context)

def new(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'new.html', context)

def new2(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'new2.html', context)

def new3(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'new3.html', context)

def new4(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'new4.html', context)