from blog.config.settings.base import *
import os
import environ

DEBUG = True

env = environ.Env()

SECRET_KEY = env('SECRET_KEY')
POSTGRES_DB = env('POSTGRES_DB')
POSTGRES_HOST = env('POSTGRES_HOST')
POSTGRES_USER = env('POSTGRES_USER')
POSTGRES_PASSWORD = env('POSTGRES_PASSWORD')

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
env = environ.Env()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': POSTGRES_HOST,
        'PORT': 5432
    }
}

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'es:9200'
    },
}
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
SECRET_KEY = env('SECRET_KEY')

