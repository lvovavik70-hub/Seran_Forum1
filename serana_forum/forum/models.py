from django.db import models

# forum/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Thread(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок темы")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    is_pinned = models.BooleanField(default=False, verbose_name="Закреплена")

    class Meta:
        ordering = ['-is_pinned', '-created_at']
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts', verbose_name="Тема")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    content = models.TextField(verbose_name="Содержание сообщения")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        ordering = ['created_at']
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Сообщение от {self.author.username} в теме '{self.thread.title}'"

# Create your models here.
