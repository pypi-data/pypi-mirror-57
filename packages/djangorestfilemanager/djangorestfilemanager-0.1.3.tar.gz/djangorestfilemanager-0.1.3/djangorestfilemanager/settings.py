import os
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

VERSION = '0.0.2'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REST = 'RST'
ORIGIN_CHOICES = (
    (REST, _('REST')),
)
DEFAULT = 'DFT'
TYPE_CHOICES = (
    (DEFAULT, _('Default')),
)
FILE_UPLOAD_EVENT = getattr(settings, 'FILE_UPLOAD_EVENT', 'FILE_UPLOAD_EVENT')

UPLOADS_DIR = getattr(settings, 'FILE_DIRS', 'file/')
