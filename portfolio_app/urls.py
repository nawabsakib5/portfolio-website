from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router তৈরি করে API ViewSet গুলো রেজিস্টার করা
router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'educations', views.EducationViewSet)
router.register(r'certificates', views.CertificateViewSet)
router.register(r'contact', views.ContactMessageViewSet, basename='contact')
router.register(r'analytics', views.AnalyticsViewSet, basename='analytics')

urlpatterns = [
    # Frontend Website URL
    path('', views.home, name='home'),

    # API Endpoints
    path('api/v1/', include(router.urls)),
]