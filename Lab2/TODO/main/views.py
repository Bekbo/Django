from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from .models import Task, Profile


def index(request):
    context = {
        'todos': Task.objects.all()
    }
    return render(request, 'todos.html', context=context)


def completed_todos(request):
    todos = Task.objects.all().filter(done=True)
    context = {
        'todos': todos
    }
    return render(request, 'completedTodos.html', context=context)
