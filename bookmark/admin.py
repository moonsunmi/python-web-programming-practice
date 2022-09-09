from django.contrib import admin
from bookmark.models import BookMark
# Register your models here.


@admin.register(BookMark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

