from django.shortcuts import render
from rest_framework import viewsets
from .models import Profile, Project, Skill, Experience, Education, Certificate
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    SkillSerializer,
    ExperienceSerializer,
    EducationSerializer,
    CertificateSerializer,
)

# ── FRONTEND HTML VIEW ──
def home(request):
    context = {
        'profile': Profile.objects.first(),
        'projects': Project.objects.all(),
        'skills': Skill.objects.all().order_by('category'),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'certificates': Certificate.objects.all(),
    }
    return render(request, 'portfolio_app/home.html', context)


# ── API VIEWSETS FOR INTERACTIVE PLAYGROUND ──
class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class CertificateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer