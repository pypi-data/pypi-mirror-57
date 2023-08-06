from django.contrib.auth.models import User
from django.test import override_settings
from rest_framework import status
from django.conf import settings
from rest_framework.test import APITestCase, APIClient

from djangorestfilemanager.models import File
from django.contrib.auth.models import Permission, ContentType


@override_settings(ROOT_URLCONF='files.urls')
class TestUploadFile(APITestCase):
    def setUp(self):
        self.content_type = ContentType.objects.create(app_label='file', model='file')
        self.perm = Permission.objects.create(content_type=self.content_type, codename='download_file',
                                              name='Download File')
        self.client = APIClient()
        self.user = User.objects.create(username='LUKE', password='1234qwer1234',
                                        email='luke@sw.stwars')
        self.user.user_permissions.add(self.perm)
        self.file = open('{}/djangorestfilemanager/test/files/test.png'.format(settings.BASE_DIR), 'rb')
        self.data = {
            'file': self.file,
            'name': 'test',
            'user_name': str(self.user.username)
        }
        self.client.force_authenticate(user=self.user)
        file = {'file': (str(self.file.name), self.file, 'text/plain', {'Expires': '0'})}
        self.response = self.client.post('/files/', data=self.data, file=file)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_download_file_share(self):
        file = File.objects.first()
        file.share = True
        file.save()
        response = self.client.post('/files/{}/file/'.format(self.response.data.get('uuid')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_download_file(self):
        response = self.client.post('/files/{}/file/'.format(self.response.data.get('uuid')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_download_file_custom_permission_share(self):
        file = File.objects.first()
        file.share = True
        file.permission = '{}.{}'.format(self.perm.content_type, self.perm.codename)
        file.save()
        response = self.client.post('/files/{}/file/'.format(self.response.data.get('uuid')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_download_file_custom_permission(self):
        file = File.objects.first()
        file.permission = '{}.{}'.format(self.perm.content_type, self.perm.codename)
        file.save()
        response = self.client.post('/files/{}/file/'.format(self.response.data.get('uuid')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_download_file_wrong_custom_permission(self):
        file = File.objects.first()
        file.permission = 'wolas'
        file.save()
        response = self.client.post('/files/{}/file/'.format(self.response.data.get('uuid')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_download_file_wrong_custom_permission_share(self):
        file = File.objects.first()
        file.permission = 'wolas'
        file.share = True
        file.save()
        response = self.client.post('/files/{}/file/'.format(self.response.data.get('uuid')))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_download_file_wrong_custom_permission_is_superuser(self):
        file = File.objects.first()
        file.permission = 'wolas'
        file.save()
        self.user.is_superuser = True
        self.user.save()
        response = self.client.post('/files/{}/file/'.format(self.response.data.get('uuid')))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_download_file_wrong_user_name_share(self):
        file = File.objects.first()
        file.user_name = 'Chewaca'
        file.permission = 'wolas'
        file.save()
        response = self.client.post('/files/{}/file/'.format(self.response.data.get('uuid')))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_download_file_not_authenticated(self):
        self.client.logout()
        response = self.client.post('/files/{}/file/'.format(self.response.data.get('uuid')))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
