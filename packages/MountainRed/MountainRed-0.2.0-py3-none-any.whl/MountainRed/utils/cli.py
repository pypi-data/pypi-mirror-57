import importlib
import os
import sys

import fire

from MountainRed.utils import show_version


def manage():
    """ 
    Run django manage.py
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MountainRed.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    args = [''] + sys.argv[2:]
    execute_from_command_line(args)


def entry_point():
    fire.Fire({
        'version': show_version,
        'manage': manage
    })
