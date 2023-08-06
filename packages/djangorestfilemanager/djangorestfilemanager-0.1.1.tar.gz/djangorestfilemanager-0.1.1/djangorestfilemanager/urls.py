from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from djangorestfilemanager.views import FileModelViewSet
from main.views import TasksView

router = routers.DefaultRouter()
router.register(r'files', FileModelViewSet)

urlpatterns = [
    path('tasks/', TasksView.as_view()),
    url(r'^', include(router.urls)),
]
