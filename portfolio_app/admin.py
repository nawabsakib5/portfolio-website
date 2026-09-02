from django.contrib import admin
from .models import Profile, Project, Skill, Experience, Education

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)