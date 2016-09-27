"""
Django settings for manosxgotas project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import random
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.abspath(__file__), '../..'),
)

# Clave secreta del proyecto.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', ''.join([random.SystemRandom()
                            .choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
                            for i in range(50)]))

# Clave de seguridad 'SALT' de itsdangerous.
SECURITY_PASSWORD_SALT = os.environ.get('DJANGO_SECURITY_PASSWORD_SALT', ''.join([random.SystemRandom()
                                        .choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
                                        for i in range(50)]))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'aplicaciones.base',
    'aplicaciones.cuentas',
    'aplicaciones.donantes',
    'aplicaciones.direcciones',
    'aplicaciones.solicitudes',

    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'sslserver',
    'geoposition',
]

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'

REST_USE_JWT = True

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'aplicaciones.cuentas.api.serializers.RegistroSerializer',
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'DATE_INPUT_FORMATS': [
        '%d/%m/%Y'
    ],

    'DATETIME_INPUT_FORMATS': [
        '%d/%m/%Y %H:%M'
    ],

    'COERCE_DECIMAL_TO_STRING': False
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'manosxgotas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_ROOT + 'aplicaciones/base/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'manosxgotas.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', 'postgresdb'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', '1234'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_ALGORITHM': 'HS256',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',

    'JWT_VERIFY': True,
}

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Mendoza'

USE_I18N = True

USE_L10N = True

USE_TZ = False

CORS_ORIGIN_ALLOW_ALL = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

BROKER_URL = os.environ.get('BROKER_URL', 'amqp://guest:guest@localhost//')

FRONTEND_URL = os.environ.get('FRONTEND_URL', 'http://localhost:8100/#/')

# Configuración email
EMAIL_PORT = 587
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = os.environ.get('MAILGUN_ACCESS_KEY')
MAILGUN_SERVER_NAME = os.environ.get('MAILGUN_SERVER_NAME')
DEFAULT_FROM_EMAIL = 'staff@manosxgotas.org'
EMAIL_USE_TLS = True

# Google maps
GEOPOSITION_GOOGLE_MAPS_API_KEY = os.environ.get('GEOPOSITION_GOOGLE_MAPS_API_KEY')
GEOPOSITION_MAP_OPTIONS = {
    'center': {'lat': -32.8897586, 'lng': -68.8445271},
    'minZoom': 5,
    'maxZoom': 16,
    'zoom': 13
}
GEOPOSITION_MARKER_OPTIONS = {
    'position': {'lat': -32.8897586, 'lng': -68.8445271},
}
