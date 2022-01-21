from .base import *

DEBUG = True

SITE_URL = "localhost:8000"

DATABASES = {
    "default": {
        "ENGINE": DB_ENGINE,
        "NAME": DB_NAME,
        "USER": "myuser",
        "PASSWORD": "mypass",
        "HOST": "localhost",
        "PORT": "5432",
    },
    "readonly": {
        "ENGINE": DB_ENGINE,
        "NAME": DB_NAME,
        "USER": "myuser",
        "PASSWORD": "mypass",
        "HOST": "localhost",
        "PORT": "5432",
    },
}
