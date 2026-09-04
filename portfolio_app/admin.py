from django.contrib import admin
from .models import (
    Profile, Project, ProjectMedia, Skill, Experience, 
    Education, Certificate, ContactMessage, Analytics
)

# --- INLINE MEDIA FOR PROJECTS ---
class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectMediaInline]
    list_display = ('title', 'tech_used', 'created_at')

# --- BASIC MODELS REGISTRATION ---
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Certificate)

# --- ADVANCED MODELS REGISTRATION ---
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('projects_built', 'apis_designed', 'uptime_percentage', 'git_commits', 'cv_downloads')