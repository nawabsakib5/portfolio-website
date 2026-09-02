from django.shortcuts import render
from .models import Profile, Project, Skill, Experience, Education

def home(request):
    context = {
        'profile': Profile.objects.first(),
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
    }
    return render(request, 'portfolio_app/home.html', context)