from django.db import models
from django.utils.timezone import now

class Verse(models.Model):
    THEMES = [
        ('love', 'Любов'),
        ('creativity', 'Творчість'),
        ('life', 'Життя'),
    ]

    title = models.CharField(max_length=255, verbose_name='Назва вірша')
    author = models.CharField(max_length=255, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст вірша')
    theme = models.CharField(
        max_length=50,
        choices=THEMES,
        verbose_name='Тема'
    )
    created_at = models.DateTimeField(default=now, verbose_name='Дата створення')

    def __str__(self):
        return f"{self.title} ({self.author})"
