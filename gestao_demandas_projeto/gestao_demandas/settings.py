"""
Django settings for gestao_demandas project.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-k$55__9!(^05&35b@%a9$_hw4nt#ed^l#4%+cxw9$%dczsomov')

# Configuração de DEBUG
IS_RAILWAY = os.environ.get('RAILWAY_ENVIRONMENT') or os.environ.get('RAILWAY_PUBLIC_DOMAIN')
if IS_RAILWAY:
    DEBUG = False
else:
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# ALLOWED_HOSTS - CORRIGIDO
RAILWAY_DOMAIN = os.environ.get('RAILWAY_PUBLIC_DOMAIN')
ALLOWED_HOSTS = [
    '10.1.25.101',
    'localhost',
    '127.0.0.1',
    '.railway.app',  # MUDOU: ponto em vez de asterisco
]

if RAILWAY_DOMAIN:
    ALLOWED_HOSTS.append(RAILWAY_DOMAIN)

if DEBUG:
    ALLOWED_HOSTS.append('*')

# CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = [
    'http://10.1.25.101:8000',
    'http://10.1.25.101:8080',
    'http://10.1.25.101:3000',
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:3000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:3000',
]

if RAILWAY_DOMAIN:
    CSRF_TRUSTED_ORIGINS.extend([
        f'https://{RAILWAY_DOMAIN}',
    ])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demandas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestao_demandas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gestao_demandas.wsgi.application'

# Database
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
    print(f"✅ Usando PostgreSQL via DATABASE_URL: {DATABASE_URL[:30]}...")
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    print("✅ Usando SQLite para desenvolvimento local")

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Para desenvolvimento: usar arquivos estáticos diretamente
if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Diretórios de arquivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'demandas' / 'static',
]

# Ensure static directories exist
for static_dir in STATICFILES_DIRS:
    if not static_dir.exists():
        static_dir.mkdir(parents=True, exist_ok=True)

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Login URLs
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'