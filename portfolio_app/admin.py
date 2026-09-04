from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Certificate)

# --- NEW MODELS REGISTRATION ---
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('projects_built', 'apis_designed', 'uptime_percentage', 'git_commits', 'cv_downloads')