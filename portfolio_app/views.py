from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .models import (
    Profile, Project, Skill, Experience, 
    Education, Certificate, ContactMessage, Analytics
)
from .serializers import (
    ProfileSerializer, ProjectSerializer, SkillSerializer,
    ExperienceSerializer, EducationSerializer, CertificateSerializer,
    ContactMessageSerializer, AnalyticsSerializer
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


# ── API VIEWSETS FOR PLAYGROUND ──
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


# ── CONTACT API WITH RATE LIMITING & EMAIL NOTIFICATION ──
class ContactThrottle(AnonRateThrottle):
    scope = 'contact'

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    throttle_classes = [ContactThrottle]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        instance = serializer.instance
        
        # অটোমেটিক ইমেইল নোটিফিকেশন পাঠানো
        subject = f"New Portfolio Message from {instance.name}: {instance.subject}"
        message = f"Sender Name: {instance.name}\nSender Email: {instance.email}\n\nMessage:\n{instance.message}"
        
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@portfolio.com'),
                recipient_list=[getattr(settings, 'NOTIFY_EMAIL', 'your_email@gmail.com')],
                fail_silently=True,
            )
        except Exception:
            pass

        return Response(
            {"message": "Thank you! Your message has been sent successfully."},
            status=status.HTTP_201_CREATED
        )


# ── ANALYTICS API VIEWSET ──
class AnalyticsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer