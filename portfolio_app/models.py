from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)  # ← এটা যোগ করো

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_used = models.CharField(max_length=200, help_text="Comma separated, e.g. Django, Python, Bootstrap")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Skill(models.Model):
    name = models.CharField(max_length=100)
    CATEGORY_CHOICES = [
        ('language', 'Language'),
        ('framework', 'Framework'),
        ('tool', 'Tool'),
        ('other', 'Other'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return self.name


class Experience(models.Model):
    role = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    start_date = models.CharField(max_length=50, help_text="e.g. Jan 2024")
    end_date = models.CharField(max_length=50, help_text="e.g. Present", blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0, help_text="Lower number shows first")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.role} at {self.organization}"


class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    year = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certificate(models.Model):
    title = models.CharField(max_length=200, help_text="e.g. Web Application Development with Python")
    issuer = models.CharField(max_length=150, help_text="e.g. NSDA")
    level = models.CharField(max_length=50, blank=True, help_text="e.g. Level-4, 360 hours")
    year = models.CharField(max_length=50, blank=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


