from django.db import models
from django.utils.timezone import now

class RandomNumber(models.Model):
    GENERATION_MODES = [
        ('single', 'Single'),
        ('range', 'Range'),
        ('set', 'Set'),
    ]

    mode = models.CharField(
        max_length=10,
        choices=GENERATION_MODES,
        default='single',
        verbose_name='Тип генерации'
    )
    result = models.TextField(verbose_name='Результат генерации')
    created_at = models.DateTimeField(default=now, verbose_name='Время создания')

    def __str__(self):
        return f"[{self.get_mode_display()}] {self.result} ({self.created_at})"