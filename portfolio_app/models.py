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
    




from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="খালি রাখলে Name অনুযায়ী অটো আইকন সেট হবে।"
    )
    
    CATEGORY_CHOICES = [
        ('language', 'Language'),
        ('framework', 'Framework'),
        ('tool', 'Tool'),
        ('other', 'Other'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

    @property
    def get_icon_class(self):
        
        if self.icon_class:
            return self.icon_class
        
        name_lower = self.name.lower().strip()
        
        # ছবিতে থাকা প্রতিটি আইটেমের জন্য Devicon ক্লাসের লিস্ট
        mapping = {
            # Framework
            'django': 'devicon-django-plain colored',
            
            # Language
            'css': 'devicon-css3-plain colored',
            'html': 'devicon-html5-plain colored',
            'python': 'devicon-python-plain colored',
            'sql': 'devicon-sqldeveloper-plain colored',
            
            # Tool
            'celery / redis': 'devicon-redis-plain colored',
            'redis': 'devicon-redis-plain colored',
            'cloudinary': 'devicon-canva-original colored', # Cloudinary এর লোগো না থাকলে এরুপ ব্যবহার করা যায়
            'git & github': 'devicon-github-original colored',
            'git': 'devicon-git-plain colored',
            'github': 'devicon-github-original colored',
            'gunicorn': 'devicon-python-plain colored',
            'postgresql': 'devicon-postgresql-plain colored',
            'render': 'devicon-express-original colored',
            'sqlite': 'devicon-sqlite-plain colored',
            'whitenoise': 'devicon-django-plain colored',
            
            # Other
            'database design': 'devicon-postgresql-plain colored',
            'graphic design (freelancing)': 'devicon-figma-plain colored',
        }
        
        
        return mapping.get(name_lower, f"devicon-{name_lower.replace(' ', '')}-plain colored")


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


