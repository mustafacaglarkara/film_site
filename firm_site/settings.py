from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-bjg_i73khlce3e+y%^6&s7io7mcrvw68-qlr)g&-ymeh%94oit"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "modeltranslation",
    "debug_toolbar",
    "admin_panel",
    "blog",
    "shared",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "firm_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
            ],
        },
    },
]

WSGI_APPLICATION = "firm_site.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "firm_site",
        "USER": "root",
        "PASSWORD": "Sas231198__",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "tr"  # Varsayılan dil Türkçe

TIME_ZONE = "Europe/Istanbul"

USE_I18N = True  # Uluslararasılaştırma
USE_L10N = True  # Yerelleştirme
USE_TZ = True

# Bu ayar, içeriği dile göre otomatik değiştirmek için kullanılabilir
# Aktif dil değiştirildiğinde sayfanın içeriği otomatik olarak güncellenecektir
LOCALE_PATHS = [
    BASE_DIR / "locale",  # proje dizinindeki locale klasörü
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "static/backend",
    BASE_DIR / "static/frontend",
    BASE_DIR / "static/shared",
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Dil ayarları
LANGUAGES = [
    ("tr", "Türkçe"),
    ("en", "English"),
]

# Dil ayarları için Django varsayılan değerler
LANGUAGE_COOKIE_NAME = "django_language"
LANGUAGE_COOKIE_AGE = 60 * 60 * 24 * 30  # 30 gün
LANGUAGE_COOKIE_PATH = "/"  # Tüm yollar için
LANGUAGE_COOKIE_DOMAIN = None  # Tüm alt alanlar için None
LANGUAGE_COOKIE_SECURE = False  # Sadece HTTPS
LANGUAGE_COOKIE_HTTPONLY = False  # JavaScript erişebilir
LANGUAGE_COOKIE_SAMESITE = "Lax"  # Cross-site request

# Cache sistemi (geliştirme için)
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

# Debug Toolbar için gerekli ayarlar
INTERNAL_IPS = [
    "127.0.0.1",
]

# Debug için log ayarları
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "shared": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
