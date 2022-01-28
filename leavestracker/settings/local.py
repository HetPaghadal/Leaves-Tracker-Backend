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

SLACK_URL = 'https://hooks.slack.com/services/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'
