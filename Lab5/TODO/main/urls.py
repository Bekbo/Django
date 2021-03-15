from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import index, TaskViewSet, TodoGroupViewSet
from rest_framework import routers
router = routers.SimpleRouter()
router.register('todos', TodoGroupViewSet, basename='groups')
router.register('list', TaskViewSet, basename='todos')
urlpatterns = [
    path('', index),
]
urlpatterns += router.urls
