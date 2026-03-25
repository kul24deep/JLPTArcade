DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5433",
    }
}

"""
JLPTarcade — Development Settings
Extends base.py with dev-friendly settings.
Never use these in production.
"""

from .base import *  # noqa: F401, F403

# ─── Debug ───────────────────────────────────────────────────────────────────
DEBUG = True

# ─── Allow all hosts in dev ───────────────────────────────────────────────────
ALLOWED_HOSTS = ["*"]

# ─── Dev-only apps ───────────────────────────────────────────────────────────
INSTALLED_APPS += [  # noqa: F405
    # Add django-debug-toolbar here if needed:
    # "debug_toolbar",
]

# ─── CORS: Allow all in dev ───────────────────────────────────────────────────
CORS_ALLOW_ALL_ORIGINS = True

# ─── Email: print to console ─────────────────────────────────────────────────
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ─── Django REST Framework: browsable API in dev ─────────────────────────────
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (  # noqa: F405
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
)

# ─── Logging ─────────────────────────────────────────────────────────────────
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] {asctime} {module} — {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "INFO",       # Set to DEBUG to log all SQL queries
            "propagate": False,
        },
    },
}