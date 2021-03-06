# -*- coding: utf-8 -*-
"""
Django settings for frikrapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7z3m$fv65qg$f+d+tiht!#(+6g!(n4g%uyq5lopsmeqlq4s@rl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photos',
    'rest_framework'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'frikrapp.urls'

WSGI_APPLICATION = 'frikrapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


LOGIN_URL = '/login'


LICENSES = (
    ('CC1', 'Creative Commons 1'),
    ('CC2', 'Creative Commons 2'),
    ('CC3', 'Creative Commons 3'),
    ('CC4', 'Creative Commons 4'),
)

# listado de tacos
BADWORDS = (u'afinabanjos', u'mascachapas', u'abrazafarolas')


# configuracion de rest framework
REST_FRAMEWORK = {
    'PAGINATE_BY' : 5,
    'MAX_PAGINATE_BY' : 10,
    'PAGINATE_BY_PARAM' : 'page_size',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer', # para JSON
        'rest_framework.renderers.XMLRenderer',  # para XML, hay que añadir la cabecera Accept: application/xml
        'rest_framework.renderers.BrowsableAPIRenderer',  # para API Navigable
    )
}

# Habilitamos la carpeta media donde se suben los archivos desde el API
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/' # http://127.0.0.1:8000/media/<whatever>


# Welcome e-mail settings
WELCOME_EMAIL_SUBJECT = 'Bienvenido a Frikr {0} {1}!'
WELCOME_EMAIL_FROM = 'hola@frikr.com'

# E-mail host settings
# https://docs.djangoproject.com/en/1.6/topics/email/
# Para desarrollo: https://docs.djangoproject.com/en/1.6/topics/email/#configuring-email-for-development
# Ejecutar en una consola python -m smtpd -n -c DebuggingServer localhost:1025 para depurar el correo
EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = '1025'


# Usar GMail como sistema de envío de e-mail
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'tu.cuenta@gmail.com'
#EMAIL_HOST_PASSWORD = 'la.de.tu.cuenta'
#EMAIL_PORT = 587
