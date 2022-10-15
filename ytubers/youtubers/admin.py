from django.contrib import admin
from django.utils.html import format_html

from .models import Youtuber


class YtAdmin(admin.ModelAdmin):

    def myphoto(self, obj):
        return format_html('<img src="{}" width="40" />'.format(obj.photo.url))

    list_display = ('id', 'name', 'myphoto', 'subs_count', 'is_featured')
    search_fields = ('name', 'camera_type')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)



admin.site.register(Youtuber, YtAdmin)