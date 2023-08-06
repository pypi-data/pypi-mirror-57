from setuptools import setup, find_packages

setup(name='djangorestfilemanager',
      version='0.1.0',
      description='Django REST File Manager',
      url='https://gitlab.com/kas-factory/packages/django-rest-file-manager',
      author='Avelino @ KF',
      author_email='avelino@kasfactory.net',
      license='MIT',
      packages=find_packages(),
      package_data={
          'djangorestfilemanager': ['djangorestfilemanager/*',
                                    'djangorestfilemanager/migrations/*',
                                    'djangorestfilemanager/locale/en/LC_MESSAGES/django.po',
                                    'djangorestfilemanager/locale/es/LC_MESSAGES/django.po',
                                    'djangorestfilemanager/locale/en/LC_MESSAGES/django.mo',
                                    'djangorestfilemanager/locale/es/LC_MESSAGES/django.mo',
                                    'djangorestfilemanager/test/*'
                                    ]
      },
      install_requires=[
          'Django',
          'djangorestframework',
          'django-storages',
          'django-filter',
          'django-cleanup',
          'djangopubsub',
          'boto3',
          'environ'
      ],
      zip_safe=False
      )
