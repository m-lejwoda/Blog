from blog.config.settings.base import *
import environ

env = environ.Env()
DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = env('SECRET_KEY')
POSTGRES_DB = env('POSTGRES_DB')
POSTGRES_HOST = env('POSTGRES_HOST')
POSTGRES_USER = env('POSTGRES_USER')
POSTGRES_PASSWORD = env('POSTGRES_PASSWORD')

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
        'hosts': 'production_es:9200'
    },
}
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
STATIC_ROOT = str(ROOT_DIR / "static")
MEDIA_ROOT = str(ROOT_DIR / "static/images")