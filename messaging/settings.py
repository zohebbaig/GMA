import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH,'static')
DATABASE_PATH = os.path.join(PROJECT_PATH, 'GMA.db')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&x*i(2hbh*7mqmws%e98shen8^gc*74rxz@i(ejrcat(b146@7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SITE_ID = 1


ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'zohebbaig.pythonanywhere.com']

LOGIN_URL = '/login/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'messaging',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'messaging.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}

# Internationalization
LANGUAGE_CODE = 'en-uk'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media') # Absolute path to the media directory

STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    STATIC_PATH,
)

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)
