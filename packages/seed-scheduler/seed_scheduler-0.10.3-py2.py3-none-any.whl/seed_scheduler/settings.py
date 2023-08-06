"""
Django settings for seed_scheduler project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import mimetypes
import os

import dj_database_url
import djcelery
from kombu import Exchange, Queue

# Support SVG on admin
mimetypes.add_type("image/svg+xml", ".svg", True)
mimetypes.add_type("image/svg+xml", ".svgz", True)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "REPLACEME")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    # admin
    "django.contrib.admin",
    # core
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party
    "raven.contrib.django.raven_compat",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "rest_hooks",
    "djcelery",
    "django_prometheus",
    # us
    "scheduler",
)

MIDDLEWARE = (
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
)

ROOT_URLCONF = "seed_scheduler.urls"

WSGI_APPLICATION = "seed_scheduler.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get(
            "SCHEDULER_DATABASE", "postgres://postgres:@localhost/seed_scheduler"
        ),
        engine="django_prometheus.db.backends.postgresql",
    )
}

PROMETHEUS_EXPORT_MIGRATIONS = False


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

STATIC_ROOT = "staticfiles"
STATIC_URL = "/static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# Sentry configuration
RAVEN_CONFIG = {
    # DevOps will supply you with this.
    "dsn": os.environ.get("SCHEDULER_SENTRY_DSN", None)
}

# REST Framework conf defaults
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.CursorPagination",
    "PAGE_SIZE": 1000,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
}

# Webhook event definition
HOOK_EVENTS = {
    # 'any.event.name': 'App.Model.Action' (created/updated/deleted)
    "schedule.added": "scheduler.Schedule.created+"
}

HOOK_DELIVERER = "scheduler.tasks.deliver_hook_wrapper"

HOOK_AUTH_TOKEN = os.environ.get("HOOK_AUTH_TOKEN", "REPLACEME")

# Celery configuration options
CELERY_RESULT_BACKEND = "djcelery.backends.database:DatabaseBackend"
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

BROKER_URL = os.environ.get("BROKER_URL", "redis://localhost:6379/0")

CELERY_DEFAULT_QUEUE = "seed_scheduler"
CELERY_QUEUES = (
    Queue("seed_scheduler", Exchange("seed_scheduler"), routing_key="seed_scheduler"),
)

CELERY_ALWAYS_EAGER = False

# Tell Celery where to find the tasks
CELERY_IMPORTS = ("scheduler.tasks",)

CELERY_CREATE_MISSING_QUEUES = True
CELERY_ROUTES = {
    "celery.backend_cleanup": {"queue": "mediumpriority"},
    "scheduler.tasks.DeliverHook": {"queue": "priority"},
    "seed_scheduler.scheduler.tasks.queue_tasks": {"queue": "priority"},
    "seed_scheduler.scheduler.tasks.requeue_failed_tasks": {"queue": "priority"},
    "seed_scheduler.scheduler.tasks.deliver_task": {"queue": "lowpriority"},
    "seed_scheduler.scheduler.tasks.fire_metric": {"queue": "metrics"},
}

METRICS_REALTIME = [
    "schedules.created.sum",
    "scheduler.deliver_task.connection_error.sum",
    "scheduler.deliver_task.http_error.400.sum",
    "scheduler.deliver_task.http_error.401.sum",
    "scheduler.deliver_task.http_error.403.sum",
    "scheduler.deliver_task.http_error.404.sum",
    "scheduler.deliver_task.http_error.500.sum",
    "scheduler.deliver_task.timeout.sum",
]
METRICS_SCHEDULED = []
METRICS_SCHEDULED_TASKS = []

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_IGNORE_RESULT = True
CELERYD_MAX_TASKS_PER_CHILD = 50

djcelery.setup_loader()

METRICS_URL = os.environ.get("METRICS_URL", None)
METRICS_AUTH = (
    os.environ.get("METRICS_AUTH_USER", "REPLACEME"),
    os.environ.get("METRICS_AUTH_PASSWORD", "REPLACEME"),
)

DEFAULT_REQUEST_TIMEOUT = float(os.environ.get("DEFAULT_REQUEST_TIMEOUT", 30))
DEFAULT_CLOCK_SKEW_SECONDS = int(os.environ.get("DEFAULT_CLOCK_SKEW_SECONDS", 5))
