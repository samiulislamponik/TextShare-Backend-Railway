from text_share.settings import *

from decouple import config
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['web-production-a568.up.railway.app']