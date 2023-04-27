
import os
from text_share.settings import *
from decouple import config

# For Deployment
DEBUG = False

SECRET_KEY = config('SECRET_KEY')

# This is allowing our deployment host
ALLOWED_HOSTS = ['web-production-a568.up.railway.app']

# This portion is for accessing the admin panel
CSRF_TRUSTED_ORIGINS = ['https://web-production-a568.up.railway.app']

# This portion is connecting the database: postgresql
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
        'OPTIONS': {'sslmode': 'require'},
    }
}



# For collecting all the static file into one folder: python manage_rail.py collectstatic
# This Portion is for WhiteNoise
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
