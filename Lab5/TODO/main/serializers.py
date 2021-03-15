from rest_framework import serializers
from main.models import Task, TaskGroup, Profile
from auth_.serializers import UserSerializer


class TaskGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskGroup
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    group = TaskGroupSerializer()

    class Meta:
        model = Task
        fields = '__all__'

