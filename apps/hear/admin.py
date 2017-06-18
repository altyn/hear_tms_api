from django.contrib import admin
from .models import Hear, Melody


# Register your models here.
@admin.register(Hear)
class HearAdmin(admin.ModelAdmin):
    list_display = ('id', 'song', 'mpfile',)

    def has_add_permission(self, request):
        return False


@admin.register(Melody)
class MelodyAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'song', 'track_id')
