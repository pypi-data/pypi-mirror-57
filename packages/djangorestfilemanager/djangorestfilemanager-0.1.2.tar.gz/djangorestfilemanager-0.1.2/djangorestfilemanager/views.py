# -*- coding: utf-8 -*-
from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status, mixins
from djangorestfilemanager.models import File
from djangorestfilemanager.filters import FileFilter
from djangorestfilemanager.serializers import FileSerializer, FileViewSerializer
import logging

logger = logging.getLogger(__name__)


# Create your views here.


class FileModelViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filter_class = FileFilter
    search_fields = ['name', 'uuid']
    ordering_fields = ['name', 'uuid', 'user_name', 'origin', 'type']
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FileViewSerializer
        return FileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        instance = serializer.instance
        serializer = FileViewSerializer(instance, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'], url_path='list-files', permission_classes=[IsAdminUser, IsAuthenticated])
    def list_files(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def file(self, request, pk, *args, **kwargs):
        object = self.get_object()
        if not request.user.is_superuser:
            if not object.share:
                if object.user_name != request.user.username:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:

                if object.permission and not request.user.has_perm(object.permission):
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
        filename = object.file.name.split('/')[-1]
        response = HttpResponse(object.file, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        logger.info('- File uuid: {}, download by user {}'.format(object.uuid, request.user.username))
        return response
