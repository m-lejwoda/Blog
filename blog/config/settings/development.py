from blog.config.settings.base import *

DEBUG=False

try:
    from blog.config.settings.local import *
except:
    pass