from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

ALLOWED_HOSTS = ["47.92.78.90"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False