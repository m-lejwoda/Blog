import os
import environ

print(os.environ)
# ENV_PATH = '/code/.envs'
env = environ.Env()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'local',
        'USER': 'local',
        'PASSWORD': 'local',
        'HOST': 'local',
        'PORT': 5432
    }
}
# environ.Env.read_env(os.path.join(ENV_PATH, '.local/.django'))
SECRET_KEY = env('SECRET_KEY')
# POSTGRES_DB = env('POSTGRES_DB')
from blog.config.settings.base import *
