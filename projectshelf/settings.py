import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-placeholder'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'users',
    'portfolio',
    'analytics',
    'rest_framework.authtoken'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    "https://site--backend--wwcs7tcpkv46.code.run",
    "https://site--frontend--wwcs7tcpkv46.code.run",
    "site--backend--wwcs7tcpkv46.code.run"]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://your-frontend-domain.com",
    "https://site--backend--wwcs7tcpkv46.code.run",
    "site--backend--wwcs7tcpkv46.code.run"
]
CORS_ALLOW_CREDENTIALS = True  
ROOT_URLCONF = 'projectshelf.urls'
CORS_ALLOW_ALL_ORIGINS = True

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
    ]},
}]

WSGI_APPLICATION = 'projectshelf.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.User'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # Accept JWTs in Authorization: Bearer <token>
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # (Optional) fall back on session auth if you also want browseable API
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'BLACKLIST_AFTER_ROTATION': True,
}


REST_USE_JWT = True

REST_AUTH_REGISTER_PERMISSION_CLASSES = (
    'rest_framework.permissions.AllowAny',
)

# Don’t require or send any confirmation e-mails
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']
ACCOUNT_EMAIL_VERIFICATION = "none"    # or "mandatory" if you want console emails
CCOUNT_LOGIN_METHODS = {'username'}
# If you’re on django-allauth ≥0.58, also define:
ACCOUNT_LOGIN_METHODS = ['username']

# Still use console backend (safer than attempting SMTP)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEBUG = True
ALLOWED_HOSTS = ['*']  # or your custom domain later
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    "https://site--backend--wwcs7tcpkv46.code.run",
    "https://site--frontend--wwcs7tcpkv46.code.run"]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://your-frontend-domain.com",
    "https://site--backend--wwcs7tcpkv46.code.run",
]
CORS_ALLOW_CREDENTIALS = True  

STATIC_URL = '/static/'

# For production (important for WhiteNoise)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Optional for better static serving (recommended)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'