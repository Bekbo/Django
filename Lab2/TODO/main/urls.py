from django.urls import path, include
from .views import index, completed_todos
urlpatterns = [
    path('', index),
    path('<int:group_key>', index),
    path('<int:group_key>/completed', completed_todos),
    path('completed', completed_todos),
]
