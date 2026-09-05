import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# Render Environment Variable থেকে SECRET_KEY নিবে, না পেলে ডিফল্ট কী ব্যবহার করবে
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-mil8_pmckzjr5vtm_ia+cp@ha^p-$6dco*@ts%uuzo274(jk@y')

# Render-এ প্রডাকশনের সময় DEBUG স্বয়ংক্রিয়ভাবে False হবে
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

# Render Host সহ যেকোনো হোস্ট এলাউ করার জন্য
ALLOWED_HOSTS = ['*']

# Render-এর CSRF Protection Fix
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'rest_framework',
    'drf_spectacular',
    'portfolio_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise Middleware for Static Files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', 
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Cloudinary & WhiteNoise Storage Settings (Django 4.2+ / 5.0+ Standard Format)
# Static & Media Storage Configuration
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# django-cloudinary-storage প্যাকেজের সামঞ্জস্যতার জন্য
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Cloudinary Credentials Configuration
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME', 'dxk8k2qkg'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY', '363587151294176'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', 'r69rvAmZcxKS8L3I0C_doJPur8w'),
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@portfolio.com'
NOTIFY_EMAIL = 'nawabsakib5@gmail.com'


# Django REST Framework & Throttling Configuration
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/day',
        'contact': '3/hour',
        'user': '100/day'
    }
}


# Interactive API Playground / Documentation Settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Portfolio API Documentation',
    'DESCRIPTION': 'Interactive API Playground and endpoints documentation for Portfolio application.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'displayOperationId': True,
    },
}