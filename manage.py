#!/usr/bin/env python
import os
import sys

REQUIREMENTS: str = '%s\\requirements.txt' % os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dunes.settings")
    try:
        #UNCOMMENT TO INSTALL ALL PROJECT DEPENDENCIES
        #os.system('pip install -r %s' % REQUIREMENTS)

        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
