import os
import environ

print(os)
ENV_PATH = '/code/.envs'
env = environ.Env()
environ.Env.read_env(os.path.join(ENV_PATH, '.local/.django'))
SECRET_KEY = env('SECRET_KEY')
POSTGRES_DB = env('POSTGRES_DB')
from blog.config.settings.base import *
