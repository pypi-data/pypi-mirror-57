from django.contrib.auth.models import User
from django.test import override_settings
from rest_framework import status
from django.conf import settings
from rest_framework.test import APITestCase, APIClient
import os
from djangorestfilemanager.models import File


@override_settings(ROOT_URLCONF='djangorestfilemanager.urls')
class TestUploadFile(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(username='LUKE', password='1234qwer1234', email='luke@sw.stwars', is_staff=True,
                                        is_superuser=True)
        f = open('file.txt', 'w')
        f.write('Test')
        f.close()
        self.file = open('file.txt', 'rb')
        self.data = {
            'file': self.file,
            'name': 'test',
            'user_name': 'Luke SKW'
        }

    def test_upload_not_authenticated_file(self):
        file = {'file': (str(self.file.name), self.file, 'text/plain', {'Expires': '0'})}
        response = self.client.post('/files/', data=self.data, file=file)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.get('/files/list-files/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(File.objects.all().count(), 0)
        os.remove('file.txt')

    def test_upload_file(self):
        self.client.force_authenticate(user=self.user)
        file = {'file': (str(self.file.name), self.file, 'text/plain', {'Expires': '0'})}
        response = self.client.post('/files/', data=self.data, file=file)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/files/list-files/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 1)
        os.remove('file.txt')

    def test_list_not_superuser_file(self):
        self.test_upload_file()
        user = User.objects.first()
        user.is_superuser = False
        user.is_staff = False
        user.save()
        self.client.force_authenticate(user=user)
        response = self.client.get('/files/list-files/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
