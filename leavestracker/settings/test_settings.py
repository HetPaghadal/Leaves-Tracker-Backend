from .base import *
import logging

DATABASES = {
    "default": {
        "ENGINE": DB_ENGINE,
        "NAME": DB_NAME,
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    },
    "readonly": {
        "ENGINE": DB_ENGINE,
        "NAME": DB_NAME,
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    },
}

SECRET_KEY = "testing-key"

logging.disable(logging.CRITICAL)

CELERY_TASK_ALWAYS_EAGER = True
