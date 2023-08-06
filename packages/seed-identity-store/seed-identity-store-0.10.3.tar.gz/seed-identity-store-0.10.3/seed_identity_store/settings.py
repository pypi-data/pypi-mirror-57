"""
Django settings for seed_identity_store project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

import dj_database_url
import environ
from kombu import Exchange, Queue

env = environ.Env()

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
    "django_prometheus",
    # us
    "identities",
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

ROOT_URLCONF = "seed_identity_store.urls"

WSGI_APPLICATION = "seed_identity_store.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get(
            "IDENTITIES_DATABASE", "postgres://postgres:@localhost/seed_identity_store"
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
    "dsn": os.environ.get("IDENTITIES_SENTRY_DSN", None)
}

# REST Framework conf defaults
REST_FRAMEWORK = {
    "PAGE_SIZE": 1000,
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.CursorPagination",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "seed_identity_store.auth.CachedTokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
}

# Webhook event definition
HOOK_EVENTS = {
    # 'any.event.name': 'App.Model.Action' (created/updated/deleted)
    "optout.requested": None,
    "optin.requested": None,
    "identity.created": "identities.Identity.created+",
    "identity.max_failures": None,
}

HOOK_DELIVERER = "identities.tasks.deliver_hook_wrapper"

HOOK_AUTH_TOKEN = os.environ.get("HOOK_AUTH_TOKEN", "REPLACEME")

# Celery configuration options
CELERY_BROKER_URL = os.environ.get("BROKER_URL", "redis://localhost:6379/0")

CELERY_TASK_DEFAULT_QUEUE = "seed_identity_store"
CELERY_TASK_QUEUES = (
    Queue(
        "seed_identity_store",
        Exchange("seed_identity_store"),
        routing_key="seed_identity_store",
    ),
)

CELERY_TASK_ALWAYS_EAGER = False

# Tell Celery where to find the tasks
CELERY_IMPORTS = ("identities.tasks",)

CELERY_TASK_CREATE_MISSING_QUEUES = True
CELERY_TASK_ROUTES = {
    "celery.backend_cleanup": {"queue": "mediumpriority"},
    "identities.tasks.DeliverHook": {"queue": "priority"},
    "identities.tasks.populate_detail_key": {"queue": "priority"},
}

ADDRESS_TYPES = ["msisdn", "email"]

CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_IGNORE_RESULT = True
CELERY_WORKER_MAX_TASKS_PER_CHILD = 50

PAPERTRAIL = os.environ.get("PAPERTRAIL")
if PAPERTRAIL:
    import seed_papertrail  # noqa

    PAPERTRAIL_HOST, _, PAPERTRAIL_PORT = PAPERTRAIL.partition(":")
    LOGGING = seed_papertrail.auto_configure(
        host=PAPERTRAIL_HOST,
        port=int(PAPERTRAIL_PORT),
        system=os.environ.get("MARATHON_APP_DOCKER_IMAGE", "seed"),
        program=os.environ.get("MESOS_TASK_ID", "identity_store"),
    )


MAX_CONSECUTIVE_SEND_FAILURES = os.environ.get("MAX_CONSECUTIVE_SEND_FAILURES", 5)

CACHES = {
    "default": env.cache(default="locmemcache://"),
    "locmem": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
}
