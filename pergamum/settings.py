from os import environ
from os.path import abspath, dirname, join
from sys import argv
from configurations import Configuration

BASE_DIR = dirname(dirname(abspath(__file__)))
PROJECT_NAME = 'pergamum'
PROJECT_ENVIRONMENT_SLUG = '{}_{}'.format(PROJECT_NAME, environ.get('DJANGO_CONFIGURATION').lower())

# Detect if we are running tests.  Is this really the best way?
IN_TESTS = 'test' in argv


class RedisCache(object):
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'KEY_PREFIX': '{}_'.format(PROJECT_ENVIRONMENT_SLUG),
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                # You may want this. See https://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
                # 'IGNORE_EXCEPTIONS': True, # see
            }
        }
    }
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
    SESSION_CACHE_ALIAS = 'default'


class Common(Configuration):
    ADMINS = (
        ('Luis Fernando Barrera', 'luisfernando@informind.com'),
    )

    MANAGERS = ADMINS

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'l9PJagTIWGA6UNItsA7L!l9PJagTIWGA6UNItsA7L'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        'suit',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'raven.contrib.django.raven_compat',
        'debug_toolbar',
        'mptt',
        "taggit",
        'bootstrap3',
        'reversion',
        'suit_redactor',
        'django_extensions',
        'clear_cache',
        'pergamum.bibloi',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    ROOT_URLCONF = 'pergamum.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                join(BASE_DIR, 'templates')
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'pergamum.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/1.10/ref/settings/#databases
    # http://django-configurations.readthedocs.org/en/latest/values/#configurations.values.DatabaseURLValue
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/1.10/topics/i18n/
    LANGUAGE_CODE = 'es'

    LOCALE_PATHS = (BASE_DIR + '/pergamum/locale',)

    TIME_ZONE = 'America/Mexico_City'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.10/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = join(BASE_DIR, 'static_root')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = join(BASE_DIR, 'media')

    # Additional locations of static files
    STATICFILES_DIRS = [
        join(BASE_DIR, 'static'),
        join(BASE_DIR, 'node_modules'),
    ]

    FIXTURE_DIRS = [
        join(BASE_DIR, 'fixtures')
    ]

    TAGGIT_CASE_INSENSITIVE = True

    SUIT_CONFIG = {
        # header
        'ADMIN_NAME': 'Administrador de contenidos',
        'HEADER_DATE_FORMAT': 'l, j. F Y',
        'HEADER_TIME_FORMAT': 'H:i',

        # forms
        # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
        # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

        # menu
        'SEARCH_URL': '',
        'MENU_ICONS': {
            'sites': 'icon-leaf',
            'auth': 'icon-lock',
            'bibloi': 'icon-folder-open',
            'taggit': 'icon-tag',
        },
        'MENU_OPEN_FIRST_CHILD': False, # Default True
        'MENU_EXCLUDE': ('auth.group',),
        # 'MENU': (
        #     'sites',
        #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
        # ),

        # misc
        # 'LIST_PER_PAGE': 15
    }


    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'django.server': {
                '()': 'django.utils.log.ServerFormatter',
                'format': '[%(server_time)s] %(message)s',
            }
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'django.server': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'django.server',
            },
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'django.server': {
                'handlers': ['django.server'],
                'level': 'INFO',
                'propagate': False,
            },
        },
    }


class Dev(Common):
    DEBUG = True
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = '/tmp/app-emails'


class Deployed(RedisCache, Common):
    """
    Settings which are for a non local deployment, served behind nginx.
    """
    # django-debug-toolbar will throw an ImproperlyConfigured exception if DEBUG is
    # ever turned on when run with a WSGI server
    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    PUBLIC_ROOT = join(BASE_DIR, '../public/')
    STATIC_ROOT = join(PUBLIC_ROOT, 'static')
    MEDIA_ROOT = join(PUBLIC_ROOT, 'media')
    COMPRESS_OUTPUT_DIR = ''

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    DEFAULT_FROM_EMAIL = ''
    SERVER_EMAIL = ''


class Stage(Deployed):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
        }
    }


class Prod(Deployed):
    DEBUG = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'pergamum',
            'USER': 'www-data',
            'PASSWORD': 'Pa$$w0rd',
            'HOST': 'localhost',
        }
    }

    ALLOWED_HOSTS = ['.demo.informind.com', ]  # add deployment domain here

    #RAVEN_CONFIG = {
    #    'dsn': ''
    #}


class Prod(Deployed):
    DEBUG = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'pergamum',
            'USER': 'www-data',
            'PASSWORD': 'Pa$$w0rd',
            'HOST': 'localhost',
        }
    }

    ALLOWED_HOSTS = ['demo.informind.com', ]  # add deployment domain here

    #RAVEN_CONFIG = {
    #    'dsn': ''
    #}


class ProdDebug(Prod):
    DEBUG = True

