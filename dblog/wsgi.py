"""
WSGI config for dblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import sys
import os

from django.core.wsgi import get_wsgi_application

path = '/home/path/to/project'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dblog.settings')

application = get_wsgi_application()
