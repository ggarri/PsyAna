"""
Django settings for PsyAna project.

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
SECRET_KEY = 'te=bcpumq+7b8k9i+l1)q)-sqa65vf$y95gcakfdi^g-q!5$6w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    # ".ggarri.com",
    ".anahidalgopsicologa.es",
    ".anahidalgopsicologaonline.es",
    # ".127.0.0.1"
]


    # Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_render_partial',
    'django.contrib.sitemaps',
    'content',
    'management'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request"
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'content.middleware.MobileDetectionMiddleware'
)

ROOT_URLCONF = 'PsyAna.urls'
WSGI_APPLICATION = 'PsyAna.wsgi.application'
AUTH_USER_MODEL = "management.UserProfile"
WEBSITE_NAME = 'PsyAna'
CUSTOM_STORAGE_FOLDER = '/Public/uploading'
CUSTOM_STORAGE_FOLDER_ROOT = os.path.join(BASE_DIR, 'Public/uploading')
PENDING_PSYANA_DUMPFILE = CUSTOM_STORAGE_FOLDER_ROOT + '/psyana_dump.sql'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db_psyana',                      # Or path to database file if using sqlite3.
        'USER': 'ggarri',                      # Not used with sqlite3.
        'PASSWORD': 'kicker13',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'Public/views'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/Public/'
# STATIC_ROOT = '/var/www/psyana/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'Public'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.1and1.es'
EMAIL_HOST_USER = 'ggarri@ggarri.com'
EMAIL_HOST_PASSWORD = 'Kicker13.'
EMAIL_PORT = 587
