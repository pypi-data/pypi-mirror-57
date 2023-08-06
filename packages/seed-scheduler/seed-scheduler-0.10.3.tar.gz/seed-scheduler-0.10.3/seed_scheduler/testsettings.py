from seed_scheduler.settings import *  # noqa: F403

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "TESTSEKRET"

CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ALWAYS_EAGER = True
BROKER_BACKEND = "memory"
CELERY_RESULT_BACKEND = "djcelery.backends.database:DatabaseBackend"

METRICS_URL = "http://metrics-url"
METRICS_AUTH_TOKEN = "REPLACEME"

PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)

# REST Framework conf defaults
REST_FRAMEWORK["PAGE_SIZE"] = 2  # noqa: F405
