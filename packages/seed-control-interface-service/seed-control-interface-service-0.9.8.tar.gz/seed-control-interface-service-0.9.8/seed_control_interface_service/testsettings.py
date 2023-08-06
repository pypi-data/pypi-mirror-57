from seed_control_interface_service.settings import *  # noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'TESTSEKRET'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ALWAYS_EAGER = True
BROKER_BACKEND = 'memory'

METRICS_URL = "http://metrics-url"
METRICS_AUTH_TOKEN = "REPLACEME"

# REST Framework conf defaults
REST_FRAMEWORK['PAGE_SIZE'] = 2  # noqa
