from django.shortcuts import render
from .models import Expertise

def index(request): 
    return render(request, 'portfolio/index.html')


def expertise(request):
    expertises = Expertise.objects.all()
    return render(request, 'portfolio/expertise.html', {
        'expertise': expertise,
    })