
import os
from text_share.settings import *
from decouple import config

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


# This Portion is for WhiteNoise
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # new