from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (
    Word,
    Theme,
    Level,
    Category
)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'show_image')
    readonly_fields = ['show_image']

    def show_image(self, obj):
        return mark_safe(f'<img src="{obj.photo}" width=150 height=150 />')

    show_image.short_description = 'Photo'


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['name', 'translation', 'example', 'show_player']
    readonly_fields = ['show_player']

    def show_player(self, obj):
        return mark_safe(f'<audio controls><source src="{obj.sound}"></audio>')

    show_player.short_description = 'Play'


admin.site.register(Level)
admin.site.register(Category)
