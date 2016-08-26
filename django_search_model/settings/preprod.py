# -*- coding: utf-8 -*-

from os import environ
from os.path import normpath
from .base import *


##########################
# Database configuration #
##########################

DATABASES['default']['HOST'] = '{{ default_db_host }}'
DATABASES['default']['USER'] = '{{ default_db_user }}'
DATABASES['default']['PASSWORD'] = '{{ default_db_password }}'
DATABASES['default']['NAME'] = '{{ default_db_name }}'


############################
# Allowed hosts & Security #
############################

ALLOWED_HOSTS = [
    '.u-strasbg.fr',
    '.unistra.fr',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'ssl')


#####################
# Log configuration #
#####################

LOGGING['handlers']['file']['filename'] = '{{ remote_current_path }}/log/app.log'

##############
# Secret key #
##############

SECRET_KEY = '{{ secret_key }}'


############
# Dipstrap #
############

DIPSTRAP_VERSION = '{{ dipstrap_version }}'
DIPSTRAP_STATIC_URL += '%s/' % DIPSTRAP_VERSION
