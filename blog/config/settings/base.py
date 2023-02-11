"""
Django settings for blog project.
Generated by 'django-admin startproject' using Django 2.2.10.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.utils.translation import gettext as _
from django.utils.translation import gettext
from django.core.management.utils import get_random_secret_key
from pathlib import Path
import environ
import dj_database_url
# import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECRET_KEY='asdasdasda231asddasd'
# env = environ.Env()
# environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# print(BASE_DIR)
# print(os.path.join(BASE_DIR, 'settings/'))
# print("env")
# print(env('SECRET_KEY'))
# print("koniec env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'blogapp',
    'corsheaders',
    'rest_framework',
    'django_sass',
    'svg',
    'ckeditor',
    'ckeditor_uploader',
    'hitcount',
    'ads',
    'sekizai',
    'fontawesome_5',
    'storages',
    'cms',
    'menus',
    'treebeard',
    'debug_toolbar',
    # 'haystack'
    'django_elasticsearch_dsl',
]
CKEDITOR_UPLOAD_PATH = "uploads/"
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "cms.middleware.utils.ApphookReloadMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",

]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]
#TODO FIX it later
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2","0.0.0.0", "172.22.0.3", "172.22.0.2"]

import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# ELASTICSEARCH_DSL = {
#     'default': {
#         'hosts': 'es:9200'
#     },
# }

# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch7_backend.Elasticsearch7SearchEngine',
#         'URL': 'es:9200',
#         'INDEX_NAME': 'haystack',
#     },
# }

# WSGI_APPLICATION = 'blog.wsgi.application'
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'db',
#         'PORT': 5432
#     }
# }

# CKEDITOR_CONFIGS = {
#     'default': {
#         'skin': 'moono',
#         'toolbar_Basic': [
#             ['Source', '-', 'Bold', 'Italic']
#         ]}
# }
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar_Basic': [
#             ['Source', '-', 'Bold', 'Italic']
#         ],
#         'toolbar': 'Basic',
#     }
# }


CMS_TEMPLATES = [
    ('blogapp/dashboard.html', 'Dashboard'),
    ('blogapp/subpage.html', 'Subpage'),
    ('blogapp/main.html', 'Main'),
    ('home.html','Home'),

]


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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

CORS_ORIGIN_ALLOW = True
# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
# STATIC_ROOT = str(ROOT_DIR / "static")
# STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR , 'static'),
# )

SVG_DIRS= [
    os.path.join(ROOT_DIR , 'svg')
]

MEDIA_URL = '/images/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")
ADS_GOOGLE_ADSENSE_CLIENT = None  # 'ca-pub-xxxxxxxxxxxxxxxx'

ADS_ZONES = {
    'header': {
        'name': 'Header',
        'ad_size': {
            'xs': '720x150',
            'sm': '800x90',
            'md': '800x90',
            'lg': '800x90',
            'xl': '800x90'
        },
        'google_adsense_slot': None,  # 'xxxxxxxxx',
        'google_adsense_format': None,  # 'auto'
    },
    'content': {
        'name': 'Content',
        'ad_size': {
            'xs': '720x150',
            'sm': '800x90',
            'md': '800x90',
            'lg': '800x90',
            'xl': '800x90'
        },
        'google_adsense_slot': None,  # 'xxxxxxxxx',
        'google_adsense_format': None,  # 'auto'
    },
    'sidebar': {
        'name': 'Sidebar',
        'ad_size': {
            'xs': '720x150',
            'sm': '800x90',
            'md': '800x90',
            'lg': '800x90',
            'xl': '800x90'
        }
    }
}

ADS_DEFAULT_AD_SIZE = '720x150'

ADS_DEVICES = (
    ('xs', 'Extra small devices'),
    ('sm', 'Small devices'),
    ('md', 'Medium devices (Tablets)'),
    ('lg', 'Large devices (Desktops)'),
    ('xl', 'Extra large devices (Large Desktops)'),
)

ADS_VIEWPORTS = {
    'xs': 'd-block img-fluid d-sm-none',
    'sm': 'd-none img-fluid d-sm-block d-md-none',
    'md': 'd-none img-fluid d-md-block d-lg-none',
    'lg': 'd-none img-fluid d-lg-block d-xl-none',
    'xl': 'd-none img-fluid d-xl-block',
}
# TODO check this one
# CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
# X_FRAME_OPTIONS = "ALLOWALL"
X_FRAME_OPTIONS = 'SAMEORIGIN'
# django_heroku.settings(locals())
SITE_ID = 1
# AWS_S3_REGION_NAME = 'eu-central-1'
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
