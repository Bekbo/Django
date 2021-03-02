from django.contrib import admin
from django.contrib.auth.models import User
from .models import Task, Profile
# Register your models here.


class TaskChoiceInline(admin.StackedInline):
    model = Task
    extra = 3


def make_published(modeladmin, request, queryset):
    queryset.update(done=True)


class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Сведение о владельце', {'fields': ['title']}),
        ('Task information', {'fields': ['owner', 'due_on', 'done'], 'classes': ['collapse']})
    ]
    actions = [make_published]
    list_filter = ['done', 'owner']
    list_display = ['title', 'owner', 'created', 'due_on', 'done']


admin.site.register(Task, TaskAdmin)
admin.site.register(Profile)
