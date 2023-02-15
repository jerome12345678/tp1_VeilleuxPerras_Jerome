"""
WSGI config for tp1_VeilleuxPerras_Jerome project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tp1_VeilleuxPerras_Jerome.settings')

application = get_wsgi_application()
