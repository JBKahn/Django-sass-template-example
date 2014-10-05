# OUTSIDE OF SCHOOL PROJECT YOU SHOULD NOT COMMIT THIS.

import os

from .common import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = ['static']
STATIC_ROOT = "sitestatic"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# Database
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import dj_database_url
DATABASES = {}
DATABASES['default'] = dj_database_url.config()


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Test Email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'orlykahnmakeupartist@gmail.com'
EMAIL_HOST_PASSWORD = 'testpassword'
DEFAULT_FROM_EMAIL = 'orlykahnmakeupartist@gmail.com'

# Security
SECRET_KEY = 'u=^)5nuz)f)*svbu22kxg^(g+w2q*zk!x##o^hk7((_+87dsoc'
DEBUG = True
TEMPLATE_DEBUG = False
