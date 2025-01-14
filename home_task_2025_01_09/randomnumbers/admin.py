from django.contrib import admin
from .models import RandomNumber

@admin.register(RandomNumber)
class RandomNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'mode', 'result', 'created_at')
    list_filter = ('mode', 'created_at')
    search_fields = ('result',)