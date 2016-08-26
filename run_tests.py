# -*- coding: utf-8 -*-


import os
import sys

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_search_model.settings.unittest'
django.setup()

from django.test.runner import DiscoverRunner


"""
Run tests script
"""

test_runner = DiscoverRunner(pattern='tests.py', verbosity=2,
                             interactive=True, failfast=False)

failures = test_runner.run_tests(['django_search_model'])
sys.exit(failures)
