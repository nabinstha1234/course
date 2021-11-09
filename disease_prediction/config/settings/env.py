from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$^mfo!8it$bs@ct6g@3%+)!m6z52l%$$ql#p^c1sl#svl-e7r*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = ('127.0.0.1',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'disease_prediction',
        'USER': 'root',
        'PASSWORD': '1997',
        'HOST': 'localhost',
        'PORT': '3306 '
    }
}

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '8818f4eb20df17'
EMAIL_HOST_PASSWORD = 'b68d248e2ff5e1'
EMAIL_PORT = '2525'


# Grab it from : https://dev.trackfly.com/wp-admin/admin.php?page=wo_manage_clients
CORE_TRACKFLY_OAUTH_CLIENT_ID = ''
CORE_TRACKFLY_OAUTH_CLIENT_SECRET = ''
CORE_TRACKFLY_OAUTH_LOGIN_URL = 'http://dev.trackfly.com/oauth/' \
                                f'authorize?client_id={CORE_TRACKFLY_OAUTH_CLIENT_ID}' \
                                f'&response_type=code'
CORE_TRACKFLY_OAUTH_TOKEN_URL = 'http://dev.trackfly.com/oauth/token/'
CORE_TRACKFLY_OAUTH_USER_INFO_URL = 'http://dev.trackfly.com/oauth/me/'