from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .models import Task


def index(request):
    todos = [
        {
            'task': 'End Lab 3',
            'created': datetime.now(),
            'dueTo': datetime.now() + timedelta(days=2),
            'owner': 'admin',
            'done': True
        },
        {
            'task': 'Buy products',
            'created': datetime.now(),
            'dueTo': datetime.now() + timedelta(days=3),
            'owner': 'admin',
            'done': True
        },
        {
            'task': 'Go to the gym',
            'created': datetime.now(),
            'dueTo': datetime.now() + timedelta(hours=11),
            'owner': 'admin',
            'done': False
        },
    ]
    context = {
        'todos': Task.objects.all()
    }
    return render(request, 'todos.html', context=context)


def completed_todos(request):
    context = {
        'todos': Task.objects.all().filter(done=True)
    }
    return render(request, 'completedTodos.html', context=context)
