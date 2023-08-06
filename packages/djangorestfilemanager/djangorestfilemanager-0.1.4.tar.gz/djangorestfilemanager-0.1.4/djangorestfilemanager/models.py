# -*- coding: utf-8 -*-
import datetime
import time
import uuid
from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
# Create your models here.
from django.conf import settings
from djangopubsub import DjangoPubSub
from storages.backends.s3boto3 import S3Boto3Storage
from djangorestfilemanager.settings import UPLOADS_DIR, ORIGIN_CHOICES, REST, TYPE_CHOICES, DEFAULT, FILE_UPLOAD_EVENT
from django.core.files.storage import default_storage


class MyFileSystemStorage(S3Boto3Storage):
    def get_available_name(self, name, max_length=None):
        now = time.time()
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S-%f')
        return slugify('{}_{}'.format(name, stamp))


def get_file_system_storage():
    if settings.S3_STORAGE:
        return MyFileSystemStorage(location='files')
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
    user_name = models.CharField(
        _('User name'),
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
        _('Origin'),
        blank=True,
        null=True,
        max_length=3,
        choices=ORIGIN_CHOICES,
        default=REST
    )
    type = models.CharField(
        _('Type'),
        blank=True,
        null=True,
        choices=TYPE_CHOICES,
        max_length=3,
        default=DEFAULT
    )
    permission = models.CharField(
        _('Permission'),
        max_length=200,
        blank=True,
        null=True,
        default=''
    )
    share = models.BooleanField(
        _('Share'),
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
            'user_name': self.user_name
        }

    def save(self, *args, **kwargs):
        DjangoPubSub().emit(FILE_UPLOAD_EVENT, self.to_dict())
        super(File, self).save(*args, **kwargs)
