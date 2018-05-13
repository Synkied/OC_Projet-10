# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

from . import *



SECRET_KEY = '-~aO;| F;rE[??/w^zcumh(9'

DEBUG = False

ALLOWED_HOSTS = ['188.166.108.19']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nutellove',  # name of the db,
        'USER': 'quentin',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432',
    }
}
