from pathlib import Path
import environ 
import os 

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
env = environ.Env()
DEBUG = env.vool("DJANGO_DEBUG",False)

#Allowed Hosts definition
if DEBUG:
    ALLOWED_HOST = ['*']
else:
    ALLOWED_HOST = env.list("DJANGO_ALLOWED_HOSTS",default="emin_gnu.com")


SECRET_KEY = env("DJANGO_SECRET_KEY")


"""
Project Apps Definitions
Django Apps - Django Internal Apps
Third Party Apps - Apps installed via requirements.txt
Project Apps - Project owned / created apps

Installed Apps = Django Apps + Third Part apps + Projects Apps
"""
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
]

THIRD_PARTY_APPS = [
    "django_extensions",
    "rest_framework",
    "storages",
    "corsheaders",
    "djangoql",
    "post_office",
    "allauth",
    "allauth.account",
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    "crispy_forns",
]


PROJECT_APPS = [
    'usermodel',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Databases
DATABASES = {
    "default": env.db("DATABASE_URL")
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)


ROOT_URLCONF = 'apliku_project.urls'

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

WSGI_APPLICATION = 'apliku_project.wsgi.application'

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
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# User Model Definition
AUTH_USER_MODEL = 'usermodel.User'

TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Admin URL Definition
ADMIN_URL = env('DJANGO_ADMIN_URL', default='admin/')


# Redis Settings
REDIS_URL = env('REDIS_URL', default=None)

if REDIS_URL:
    CACHES = {
        "default": env.cache('REDIS_URL')
    }


# Redis Settings
REDIS_URL = env('REDIS_URL', default=None)

if REDIS_URL:
    CACHES = {
        "default": env.cache('REDIS_URL')
    }
