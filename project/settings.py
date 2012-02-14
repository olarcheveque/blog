import os
from django.conf import global_settings
from conf import *

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS


TIME_ZONE = 'America/Montreal'

LANGUAGE_CODE = 'fr-ca'
DATE_FORMAT = 'd M Y'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# Don't share this with anybody.
SECRET_KEY = 'nxf$j(qr-95@mtke9@*-$!=pb@ri0pb9cq*56a7#vxdca&b1ic'

ROOT_URLCONF = 'project.urls'


INSTALLED_APPS = (
    'project.skin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.staticfiles',
    'south',
    'tagging',
    'mptt',
    'zinnia',
    'project.contact',
    'sentry.client',
    'django_vu.client',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
  'django.core.context_processors.request',
  'django.core.context_processors.static',
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

ZINNIA_MAIL_COMMENT_AUTHORS = False
ZINNIA_MARKUP_LANGUAGE = 'markdown'
ZINNIA_WYSIWYG = 'markitup'
