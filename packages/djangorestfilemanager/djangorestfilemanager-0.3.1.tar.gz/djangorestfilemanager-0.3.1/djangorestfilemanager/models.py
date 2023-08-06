# -*- coding: utf-8 -*-
import datetime
import time
import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.template.defaultfilters import slugify
from django.conf import settings

from storages.backends.s3boto3 import S3Boto3Storage
from django.core.files.storage import default_storage


class RestFileManagerStorage(S3Boto3Storage):

    def get_available_name(self, name, max_length=None):
        now = time.time()
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S-%f')
        return slugify('{}_{}'.format(name, stamp))


def get_file_system_storage():
    if getattr(settings, 'S3_STORAGE'):
        return RestFileManagerStorage(location='files')
    else:
        return default_storage


class File(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True
    )
    file = models.FileField(
        verbose_name=_('File'),
        storage=get_file_system_storage()
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=100
    )
    username = models.CharField(
        _('Username'),
        max_length=100
    )
    creation_date = models.DateTimeField(
        verbose_name=_('Creation date'),
        auto_now_add=True,
    )
    last_mod_date = models.DateTimeField(
        verbose_name=_('Creation date'),
        auto_now=True,
    )
    origin = models.CharField(
        verbose_name=_('Origin'),
        blank=True,
        null=True,
        max_length=3,
        default='API'
    )
    type = models.CharField(
        verbose_name=_('Type'),
        blank=True,
        null=True,
        max_length=10,
        default='file'
    )
    permission = models.CharField(
        verbose_name=_('Permission'),
        max_length=200,
        blank=True,
        null=True,
        default=''
    )
    share = models.BooleanField(
        verbose_name=_('Share'),
        default=False
    )

    class Meta:
        verbose_name = _('File')
        verbose_name_plural = _('Files')

    def __str__(self):
        return '{}-{}'.format(self.name, self.type)

    def to_dict(self):
        return {
            'uuid': str(self.uuid),
            'name': self.name,
            'origin': self.origin,
            'type': self.type,
            'username': self.username
        }
