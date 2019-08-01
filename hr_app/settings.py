"""
Django settings for hr_app project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from google.cloud import storage

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v%$i_pvzh@68i53)awc0-ok*b97-#r^%x3&^y^20^wf4#5)5s5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "myapp",
    'storages',
    'widget_tweaks',
    'bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hr_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':[
                'bootstrap4.templatetags.bootstrap4',
            ],
        },
    },
]

WSGI_APPLICATION = 'hr_app.wsgi.application'

#DATABASES = {
#    'default': {
#        # If you are using Cloud SQL for MySQL rather than PostgreSQL, set
#        # 'ENGINE': 'django.db.backends.mysql' instead of the following.
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'mydb',
#        'USER': 'mizuhiki0111',
#        'PASSWORD': 'paul0111',
#        # SQL Proxy instances running locally must also be set to tcp:3306.
#        'PORT': '5432',
#    }
#}
# In the flexible environment, you connect to CloudSQL using a unix socket.
# Locally, you can use the CloudSQL proxy to proxy a localhost connection
# to the instance
#DATABASES['default']['HOST'] = '/cloudsql/hrproject-246507:asia-northeast1:hrsql'
#if os.getenv('GAE_INSTANCE'):
#    pass
#else:
#    DATABASES['default']['HOST'] = '127.0.0.1'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"media")


ALLOWED_HOSTS = ['*']

#STATIC_URL = '/static/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_URL = '/media/'

#ALLOWED_HOSTS = ["インスタンス名.appspot.com","127.0.0.1",'localhost']

#from google.oauth2 import service_account
#GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#    'hrapp-876db69ffa0c.json'
#)

#DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
#STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
#GS_BUCKET_NAME = 'hrbucket0111'
#GS_PROJECT_ID = 'hrapp-248505'
