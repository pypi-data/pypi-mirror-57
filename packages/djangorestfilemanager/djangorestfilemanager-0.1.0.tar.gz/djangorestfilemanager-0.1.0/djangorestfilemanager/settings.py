import os
import environ
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

VERSION = '0.0.1'

env = environ.Env(
    # security
    AWS_DEFAULT_ACL=(str, None),
    AWS_ACCESS_KEY_ID=(str, None),
    AWS_SECRET_ACCESS_KEY=(str, None),
    AWS_STORAGE_BUCKET_NAME=(str, None),
    AWS_CACHE_CONTROL=(int, 86400),
    AWS_LOCATION=(str, None),
    AWS_S3_FILE_OVERWRITE=(bool, False)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

S3_STORAGE = False
AWS_DEFAULT_ACL = None
if env('AWS_ACCESS_KEY_ID') and env('AWS_SECRET_ACCESS_KEY') and env('AWS_STORAGE_BUCKET_NAME'):
    S3_STORAGE = True
    AWS_ACCESS_KEY_ID = getattr(settings, 'AWS_ACCESS_KEY_ID', env('AWS_ACCESS_KEY_ID'))
    AWS_SECRET_ACCESS_KEY = getattr(settings, 'AWS_SECRET_ACCESS_KEY', env('AWS_SECRET_ACCESS_KEY'))
    AWS_STORAGE_BUCKET_NAME = getattr(settings, 'AWS_STORAGE_BUCKET_NAME', env('AWS_STORAGE_BUCKET_NAME'))
    AWS_LOCATION = getattr(settings, 'AWS_LOCATION', env('AWS_LOCATION'))
    AWS_S3_CUSTOM_DOMAIN = getattr(
        settings, 'AWS_S3_CUSTOM_DOMAIN', '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
    )
    AWS_S3_OBJECT_PARAMETERS = getattr(
        settings, 'AWS_S3_OBJECT_PARAMETERS', {'CacheControl': 'max-age={}'.format(env("AWS_CACHE_CONTROL"))}
    )
    AWS_S3_FILE_OVERWRITE = getattr(settings, 'AWS_S3_FILE_OVERWRITE', False)

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
