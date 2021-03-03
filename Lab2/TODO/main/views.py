from django.shortcuts import render
from .models import Task, TaskGroup


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


def completed_todos(request, group_key=""):
    group = TaskGroup
    todos = Task.objects.all()
    context = {}
    try:
        if group_key == "":
            context = {
                'todos': todos.filter(done=True),
                'group': 'All'
            }
        if group_key and group_key != "":
            group = TaskGroup.objects.get(id=group_key)
            context = {
                'todos': todos.filter(group=group_key, done=True),
                'group': group
            }
    except TaskGroup.DoesNotExist:
        context = {
            'todos': todos,
            'group': f'All [Group {group_key} does not exit]'
        }
    return render(request, 'completedTodos.html', context=context)
