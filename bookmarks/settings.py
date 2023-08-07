"""
Django settings for bookmarks project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from environs import Env
from django.urls import reverse_lazy


env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    import mimetypes
    mimetypes.add_type('application/javascript', '.js', True)
    mimetypes.add_type('text/css', '.css', True)

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
# Application definition

INSTALLED_APPS = [
    "account.apps.AccountConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'social_django',
    'django_extensions',
    'images.apps.ImagesConfig',
    'easy_thumbnails',
    'actions.apps.ActionsConfig'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "bookmarks.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "bookmarks.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: reverse_lazy('user_detail', args= [u.username])
}
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

AUTHENTICATION_BACKENDS = [
'django.contrib.auth.backends.ModelBackend',
'account.authentication.EmailAuthBackend',
'social_core.backends.facebook.FacebookOAuth2',
'social_core.backends.twitter.TwitterOAuth',
'social_core.backends.google.GoogleOAuth2',
]

SOCIAL_AUTH_PIPELINE = [
'social_core.pipeline.social_auth.social_details',
'social_core.pipeline.social_auth.social_uid',
'social_core.pipeline.social_auth.auth_allowed',
'social_core.pipeline.social_auth.social_user',
'social_core.pipeline.user.get_username',
'social_core.pipeline.user.create_user',
'account.authentication.create_profile',
'social_core.pipeline.social_auth.associate_user',
'social_core.pipeline.social_auth.load_extra_data',
'social_core.pipeline.user.user_details',
]

SOCIAL_AUTH_FACEBOOK_KEY = '818781036478937'
SOCIAL_AUTH_FACEBOOK_SECRET = 'd74a33a78b328ad8b181dd6d3967c1b2'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = 'wlqyTWiEll2FXFuQQwVr9GFyZ'
SOCIAL_AUTH_TWITTER_SECRET = '1THTkFkZhUqlyFta3xRXA8XDnXr5ug4Pg9wg1cuKsA5xXML7ol'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1002061908023-n0v5u1f9avhudcih5v6mff48kidf53ck.apps.googleusercontent.com' 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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' 
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR /'media'
THUMBNAIL_DEBUG = True