from django.conf import settings
from djangorestfilemanager.models import File
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            'url', 'uuid', 'file', 'name', 'user_name', 'creation_date', 'last_mod_date', 'permission', 'type',
            'origin', 'share'
        )
        read_only_fields = ('uuid', 'creation_date', 'last_mod_date')

    def create(self, validated_data):
        user = self.context.get('request').user
        instance = super(FileSerializer, self).create(validated_data)
        logger.info('- File uuid: {}, upload by user {}'.format(instance.uuid, user.username))
        return instance


class FileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('uuid',)
        read_only_fields = ('uuid',)
