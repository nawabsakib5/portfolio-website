from django.shortcuts import render
from .models import*

def home(request):
    context = {
        'profile': Profile.objects.first(),
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
    }
    return render(request, 'portfolio_app/home.html', context)


def home(request):
    context = {
        'profile': Profile.objects.first(),
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'certificates': Certificate.objects.all(),
    }
    return render(request, 'portfolio_app/home.html', context)