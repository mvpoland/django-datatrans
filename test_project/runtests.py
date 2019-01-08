#This file mainly exists to allow python setup.py test to work.

import os, sys
from django.test.utils import get_runner
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project.settings'

test_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, test_dir)


def runtests():
    try:
        from django import setup
        setup()
    except ImportError:
        pass

    test_runner = get_runner(settings)
    failures = test_runner().run_tests([])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
