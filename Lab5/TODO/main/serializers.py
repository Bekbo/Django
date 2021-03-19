from rest_framework import serializers
from main.models import Task, TaskGroup, Profile
from auth_.serializers import UserSerializer
from auth_.models import User


class TaskGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskGroup
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    group = TaskGroupSerializer()

    def create(self, validated_data):
        group_name = validated_data.pop('group')['name']
        group, created = TaskGroup.objects.get_or_create(name=group_name)
        owner_name = validated_data.pop('owner')['username']
        owner, created = User.objects.get_or_create(username=owner_name)
        task = Task.objects.create(**validated_data, group=group, owner=owner)
        return task

    class Meta:
        model = Task
        fields = '__all__'

