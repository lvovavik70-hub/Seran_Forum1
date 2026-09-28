"""
Django settings for serana_forum project.
SHS Project - Форум Штаты Серана
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# БЕЗОПАСНОСТЬ: ключ берем из .env
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-key-for-dev-only')
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# core/settings.py
# Найди эту строку и замени на:
ALLOWED_HOSTS = ['*']  # Для PythonAnywhere разрешаем все хосты

# НАСТРОЙКИ ПРИЛОЖЕНИЙ
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Наше приложение форума
    'forum',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Папка для общих шаблонов
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

WSGI_APPLICATION = 'core.wsgi.application'

# БАЗА ДАННЫХ (SQLite — идеально для старта и ноутбука)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ИНТЕРНАЦИОНАЛИЗАЦИЯ (русский язык, Санкт-Петербург)
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# СТАТИЧЕСКИЕ ФАЙЛЫ (CSS, JS, изображения)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Папка для твоих CSS/JS/TS файлов
STATIC_ROOT = BASE_DIR / 'staticfiles'    # Для сбора статики на хостинге

# Медиа-файлы (загрузки пользователей — пригодится для аватарок)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'