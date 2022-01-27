from .local_example import *

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
