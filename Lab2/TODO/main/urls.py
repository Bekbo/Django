from django.urls import path, include
from .views import index, completed_todos
urlpatterns = [
    path('', index),
    path('completed', completed_todos)
]
