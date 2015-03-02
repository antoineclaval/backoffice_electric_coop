from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# why : i'm serving media ( and static ) from python -m SimpleHTTPServer 8001 in BASE_DIR
MEDIA_URL = "http://localhost:8001/media/"