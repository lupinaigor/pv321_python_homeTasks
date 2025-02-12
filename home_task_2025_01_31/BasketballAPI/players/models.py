from django.db import models

class BasketballPlayer(models.Model):
    name = models.CharField(max_length=255)
    height = models.IntegerField()

    def __str__(self):
        return self.name