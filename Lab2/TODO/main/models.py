from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.


class Task(models.Model):
    DONE_CHOICE = (
        (True, "Закончено"),
        (False, "В прогрессе")
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец задачи')
    title = models.CharField(max_length=100, verbose_name="Название задачи")
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    due_on = models.DateTimeField(verbose_name='Дата выполнение')
    done = models.BooleanField(choices=DONE_CHOICE, verbose_name='Статус', default=False)

    def show_done(self):
        pass

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['created']

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    role = models.CharField(verbose_name='Должность', max_length=100, null=True)

    def __str__(self):
        return f"{self.user}' profile - {self.role}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


