"""
WSGI config for gammelnok project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gammelnok.settings")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
from opbeat.contrib.django.middleware.wsgi import Opbeat
application = get_wsgi_application()
application = Cling(application)
application = Opbeat(application)
