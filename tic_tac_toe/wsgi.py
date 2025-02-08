import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from tic_tac_toe import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tic_tac_toe.settings')
application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT) 