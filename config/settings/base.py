#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for bricksa
For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

import environ

# DIRS
# -----------------------------------------------------------------------------
ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
PROJECT_DIR = ROOT_DIR.path('bricksa')
APPS_DIR = ROOT_DIR.path('bricksa/apps')

env = environ.Env()

# PROJECT APPS
# -----------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'suit',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'bricksa.apps.projects',
    'bricksa.apps.departments',
)

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

# MIDDLEWARE CLASSES
# -----------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# MIGRATION
# -----------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'cookies.contrib.sites.migrations'
}

# FIXTURE CONFIGURATION
# -----------------------------------------------------------------------------
FIXTURE_DIRS = (
    str(PROJECT_DIR.path('fixtures')),
)

# GENERAL CONFIGURATION
# -----------------------------------------------------------------------------
TIME_ZONE = 'America/Mexico_City'

LANGUAGE_CODE = 'es'

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
)

LOCALE_PATHS = (
    str(PROJECT_DIR.path('locale')),
)

# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(PROJECT_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': True,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# URL Configuration
# -----------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# -----------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# SUIT CONFIGURATION
# -----------------------------------------------------------------------------
SUIT_CONFIG = {
    'ADMIN_NAME': 'bricksa',
}

# STATIC CONFIGURATION
# -----------------------------------------------------------------------------
STATICFILES_DIRS = (
    str(PROJECT_DIR.path('static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = str(PROJECT_DIR('staticfiles'))
