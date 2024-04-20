"""
ASGI config for logistic project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.Payment_List.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logistic.settings')

application = get_asgi_application()
