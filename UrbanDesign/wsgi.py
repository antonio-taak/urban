#!/var/www/vhosts/UrbanDesign/urban/lib/python3.8
"""
WSGI config for UrbanDesign project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

path='/var/www/vhosts/UrbanDesign'
if path not in sys.path:
  sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UrbanDesign.settings')

application = get_wsgi_application()
