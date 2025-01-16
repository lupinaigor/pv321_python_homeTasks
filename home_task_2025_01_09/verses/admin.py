from django.contrib import admin
from .models import Verse

@admin.register(Verse)
class VerseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'theme', 'created_at')
    list_filter = ('theme', 'author')
    search_fields = ('title', 'author', 'text')

