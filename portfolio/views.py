from django.shortcuts import render
from .models import Expertise, About, Gallery
from blog.models import Post, Category

def index(request): 
    latest_blog = Post.objects.last()
    category = Category.objects.all()
    gallery = Gallery.objects.all()
    return render(request, 'portfolio/index.html', {
        'latest_blog':latest_blog,
        'category': category,
        'gallery': gallery,
    })


def expertise(request):
    expertises = Expertise.objects.all()
    print(expertise)
    return render(request, 'portfolio/expertise.html', {
        'expertises': expertises,
    })

def about(request):
    about_section = About.objects.first()  # Get the first (or only) About object
    return render(request, 'portfolio/about.html', {
        "about": about_section
    })
