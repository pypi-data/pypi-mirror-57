# Django REST File Manager

A package that provides authenticated file management (upload/download) using REST Framework and Amazon S3 (optionally)


## Add app to django settings
```
INSTALLED_APPS = (
    ...,
    'djangorestfilemanager.apps.DjangoRestFileManagerConfig''
)
```


## Available settings and defaults:
djangopubsub
```python
BASE_DIR = ''  # Root directory for handlers lookup
EVENT_HANDLERS_DIR_NAME = 'event_handlers'  #  Directory with handlers on every app module
HANDLER_FILES_PREFIX = 'handlers_' # handlers file prefix
REDIS_HOST = 'localhost'
REDIS_PORT = 6379 
PUB_SUB_EMIT = True  # Avoid to emit message when emit is called (for tests)
```
djangorestfilemanager
add to .env file:
```python
AWS_DEFAULT_ACL=(str, None),
AWS_ACCESS_KEY_ID=(str, None),
AWS_SECRET_ACCESS_KEY=(str, None),
AWS_STORAGE_BUCKET_NAME=(str, None),
AWS_CACHE_CONTROL=(int, 86400),
AWS_LOCATION=(str, None),
AWS_S3_FILE_OVERWRITE=(bool, False)
```
In main setting file:
when a file is created, an 'UPLOADS_DIR' event is generated. To modify the emmit, you can declare in main settings.py
```python
FILE_UPLOAD_EVENT = ''
```


By default, the uploads files will save in dirs .../file/
````python
UPLOADS_DIR = ''
````





# How to update to Pypi

When a new release is ready we have to make the package. Exec the following command (Remember to update setup.py with the current version of the package.)

```
python setup.py sdist
```

After that, we have to push our package to Pypi with `twine` (the first time we will have to install it)

```
twine upload dist/*
```

This command will upload every version existing on dist folder, we can specify one changing `dist/*` to the new dist file `dist/package_filename.gz`. 
