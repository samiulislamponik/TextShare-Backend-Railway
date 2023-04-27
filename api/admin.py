from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TextSnippet


class TextSnippetAdmin(admin.ModelAdmin):
    fields = ['content', 'url']


admin.site.register(TextSnippet, TextSnippetAdmin)
