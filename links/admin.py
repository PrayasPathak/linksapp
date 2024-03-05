from django.contrib import admin

# Register your models here.
from .models import Link


@admin.register(Link)
class AdminLink(admin.ModelAdmin):
    list_display = ["name", "url", "slug", "clicks"]
    list_per_page = 10
    list_filter = ["id", "name"]
