from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE_DEV", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME_DEV", BASE_DIR / "db.sqlite3"),
        "USER": os.getenv("DB_USER_DEV", "user"),
        "PASSWORD": os.getenv("DB_PASS_DEV", "password"),
        "HOST": os.getenv("DB_HOST_DEV", "localhost"),
        "PORT": os.getenv("DB_PORT_DEV", "5432"),
    }
}
