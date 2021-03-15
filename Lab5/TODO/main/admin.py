from django.contrib import admin
from django.contrib.auth.models import User
from .models import Task, Profile, TaskGroup
# Register your models here.


class TaskChoiceInline(admin.StackedInline):
    model = Task
    extra = 3


def make_published(modeladmin, request, queryset):
    queryset.update(done=True)


class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Сведение о владельце', {'fields': ['owner']}),
        ('Task information', {'fields': ['title', 'group', 'due_on', 'done'], 'classes': ['collapse']})
    ]
    actions = [make_published]
    list_filter = ['group', 'done', 'owner']
    list_display = ['title', 'group', 'owner', 'created', 'due_on', 'done']


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskGroup)
admin.site.register(Profile)
