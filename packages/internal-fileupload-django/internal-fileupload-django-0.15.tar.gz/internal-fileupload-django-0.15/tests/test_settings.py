"""
https://docs.djangoproject.com/en/2.2/topics/testing/advanced/#testing-reusable-applications
"""

import os
import sys

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kjh*f8p@rhyp$3gue35z+sss9s+(6ume&4@vo1@qsg!h!%i40e6qq'

# SECURITY WARNING: don't run with debug turned on in production!
if (os.path.exists(os.path.join(BASE_DIR, 'test.cnf'))):
    ENVDEV = True
    DEBUG = True
else:
    ENVDEV = False
    DEBUG = False

ALLOWED_HOSTS = ['workhorse.icelabz.com', '127.0.0.1', 'icelabz.com', 'icelabz.co.uk', 'icelabz.test']

CORS_ORIGIN_WHITELIST = [
    "https://icelabz.test",
    "http://icelabz.test",
    "https://icelabz.com",
    "https://icelabz.co.uk",
    "http://icelabz.com",
    "http://icelabz.co.uk",
    "http://127.0.0.1:8000",

]


ROOT_URLCONF = 'tests.urls'




# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
INSTALLED_APPS = [
    "fileupload",
    "tests"
]
GOOGLE_BUCKET="clientupload-icelabz"