from blog.config.settings.base import *
import environ

# ENV_PATH = '/code/.envs'
env = environ.Env()
DEBUG = False
ALLOWED_HOSTS = ['*']
SECRET_KEY = env('SECRET_KEY')
POSTGRES_DB = env('POSTGRES_DB')
POSTGRES_HOST = env('POSTGRES_HOST')
POSTGRES_USER = env('POSTGRES_USER')
POSTGRES_PASSWORD = env('POSTGRES_PASSWORD')
# WSGI_APPLICATION = 'blog.config.wsgi_production'


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

