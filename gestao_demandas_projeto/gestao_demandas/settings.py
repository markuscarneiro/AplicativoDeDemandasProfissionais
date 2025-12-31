"""
Django settings for gestao_demandas project.

Configurações do projeto de Gestão de Demandas Profissionais.
Suporta deployment local (SQLite) e produção (PostgreSQL/Railway).

Para mais informações sobre este arquivo, veja:
https://docs.djangoproject.com/en/4.2/topics/settings/
"""

import os
from pathlib import Path


# =============================================================================
# CONFIGURAÇÕES BASE
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta - DEVE ser configurada via variável de ambiente em produção
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-k$55__9!(^05&35b@%a9$_hw4nt#ed^l#4%+cxw9$%dczsomov'
)

# Detecção de ambiente
IS_RAILWAY = bool(
    os.environ.get('RAILWAY_ENVIRONMENT') or
    os.environ.get('RAILWAY_PUBLIC_DOMAIN')
)
DEBUG = not IS_RAILWAY and os.environ.get('DEBUG', 'True').lower() == 'true'


# =============================================================================
# HOSTS E SEGURANÇA
# =============================================================================

RAILWAY_DOMAIN = os.environ.get('RAILWAY_PUBLIC_DOMAIN', '')

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '10.1.25.101',
    '.railway.app',
]

if RAILWAY_DOMAIN:
    ALLOWED_HOSTS.append(RAILWAY_DOMAIN)

if DEBUG:
    ALLOWED_HOSTS.append('*')

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:3000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:3000',
    'http://10.1.25.101:8000',
    'http://10.1.25.101:8080',
    'http://10.1.25.101:3000',
]

if RAILWAY_DOMAIN:
    CSRF_TRUSTED_ORIGINS.append(f'https://{RAILWAY_DOMAIN}')


# =============================================================================
# APLICAÇÕES INSTALADAS
# =============================================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps locais
    'demandas',
]


# =============================================================================
# MIDDLEWARE
# =============================================================================

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


# =============================================================================
# TEMPLATES
# =============================================================================

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


# =============================================================================
# BANCO DE DADOS
# =============================================================================

DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# =============================================================================
# VALIDAÇÃO DE SENHAS
# =============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =============================================================================
# INTERNACIONALIZAÇÃO
# =============================================================================

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# =============================================================================
# ARQUIVOS ESTÁTICOS
# =============================================================================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

if DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
else:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'demandas' / 'static',
]

# Criar diretórios estáticos se não existirem
for static_dir in STATICFILES_DIRS:
    if not static_dir.exists():
        static_dir.mkdir(parents=True, exist_ok=True)


# =============================================================================
# ARQUIVOS DE MÍDIA
# =============================================================================

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =============================================================================
# AUTENTICAÇÃO
# =============================================================================

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'


# =============================================================================
# SEGURANÇA
# =============================================================================

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Configurações de segurança para produção (HTTPS)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000  # 1 ano
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


# =============================================================================
# CONFIGURAÇÕES PADRÃO
# =============================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'