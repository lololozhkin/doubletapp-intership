from django.contrib import admin
from .models import (
    Word,
    Theme,
    Level,
    Category
)


admin.site.register(Word)
admin.site.register(Theme)
admin.site.register(Level)
admin.site.register(Category)
