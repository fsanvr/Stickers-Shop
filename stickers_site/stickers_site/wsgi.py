from django.core.wsgi import get_wsgi_application
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stickers_site.settings')

application = get_wsgi_application()
