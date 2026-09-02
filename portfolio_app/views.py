from django.shortcuts import render
from .models import Profile, Project

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    context = {
        'profile': profile,
        'projects': projects,
    }
    return render(request, 'portfolio_app/home.html', context)