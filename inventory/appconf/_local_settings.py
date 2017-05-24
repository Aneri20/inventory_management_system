import os
from common.settings import *

SECRET_KEY = '@pzaeeu_u+ggea4cvbhkl3b%1dhtmor3%zv4h7d5%ks38506=k'

DEBUG = True

ALLOWED_HOSTS = ['']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ims',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '10.200.1.30',
        'PORT': '5432'
    }
}


STATIC_URL = '/inventory_management_system/static/'
STATIC_ROOT = '/inventory_management_system/static/'

STATICFILES_DIRS = (
    #This lets Django's collectstatic store our bundles
    os.path.join(BASE_DIR, './static'),
)

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = ''

# Odoo settings
AUTH_ODOO_HOSTNAME = 'sterp.suitabletech.com'
AUTH_ODOO_PROTOCOL = 'xmlrpc+ssl'
AUTH_ODOO_BINDPORT = 443
AUTH_ODOO_DATABASE = 'suitable'
AUTH_ODOO_GROUPFILTER = [1]