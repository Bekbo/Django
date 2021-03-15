from django.shortcuts import render
from .models import Task, TaskGroup
from .serializers import TaskGroupSerializer, TaskSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response


def index(request, group_key=""):
    group = TaskGroup
    try:
        if group_key:
            group = TaskGroup.objects.get(id=group_key)
            context = {
                'todos': Task.objects.all().filter(group=group_key),
                'group': group
            }
        else:
            context = {
                'todos': Task.objects.all(),
                'group': 'All'
            }
    except TaskGroup.DoesNotExist:
        context = {
            'todos': Task.objects.all(),
            'group': 'All'
        }
    return render(request, template_name='todos.html', context=context)


class TodoGroupViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = TaskGroup.objects.all()
    serializer_class = TaskGroupSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def completed(self, request, pk):
        group = self.get_object()
        serializer = TaskSerializer(group.todos.filter(done=True), many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def all(self, request, pk):
        group = self.get_object()
        serializer = TaskSerializer(group.todos, many=True)
        return Response(serializer.data)


class TaskViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['GET', 'PATCH', 'PUT', 'delete'], detail=True, permission_classes=(AllowAny,))
    def edit(self, request, pk):
        item = self.queryset.get(id=pk)
        serializer = TaskSerializer(item)
        if request.method == 'PUT':
            item.title = request.data['title']
            item.done = request.data['done']
            item.save()
        return Response(serializer.data)
