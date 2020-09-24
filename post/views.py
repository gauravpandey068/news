from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Category, Post, Topbar


def index(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(status=1)
    paginator = Paginator(posts, 5)
    trendings = Post.objects.filter(trending=1)
    slides = Post.objects.filter(slideshow=1)
    tops = Post.objects.all().order_by('category__topbar')
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': categories,
        'posts': posts,
        'trendings': trendings,
        'slides': slides,
        'tops': tops,
        'page_obj': page_obj
    }

    return render(request, 'index.html', context)


def detail(request, slug):
    categories = Category.objects.all()
    trendings = Post.objects.filter(trending=1)
    tops = Post.objects.all().order_by('category__topbar')
    post = Post.objects.get(slug=slug)
    context = {
        'categories': categories,
        'trendings': trendings,
        'tops': tops,
        'post': post
    }
    return render(request, 'news-page.html', context)


def lists(request, id):
    categories = Category.objects.all()
    trendings = Post.objects.filter(trending=1)
    tops = Post.objects.all().order_by('category__topbar')
    posts = Post.objects.filter(status=1, category=id).order_by('-created_at')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    category = Category.objects.get(id=id)
    context = {
        'categories': categories,
        'trendings': trendings,
        'tops': tops,
        'posts': posts,
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'news-list.html', context)
