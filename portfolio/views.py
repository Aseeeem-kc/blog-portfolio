from django.shortcuts import render, redirect
from .models import Expertise, About, Gallery, ContactMessage
from .forms import ContactForm
from blog.models import Post, Category
from django.contrib import messages

def index(request): 
    latest_blog = Post.objects.order_by('created_on')[:2]
    category = Category.objects.all()
    gallery = Gallery.objects.all()
    about_section = About.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted.")
            return redirect(index)
    else:
        form = ContactForm()

    return render(request, 'portfolio/index.html', {
        'latest_blog':latest_blog,
        'category': category,
        'gallery': gallery,
        'form': form,
        "about": about_section
    })


def expertise(request):
    expertises = Expertise.objects.all()
    about_section = About.objects.first()
    print(expertise)
    return render(request, 'portfolio/expertise.html', {
        'expertises': expertises,
        "about": about_section
    })

def about(request):
    about_section = About.objects.first()
    return render(request, 'portfolio/about.html', {
        "about": about_section
    })


def contact_view(request):
    about_section = About.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.sucess("Your message has been submitted.")
            print('chalyo yo samma ta')
    else:
        form = ContactForm()
    
    
    return render(request, 'index.html', {
        'form': form,
        'messages': messages,
        "about": about_section
        })

