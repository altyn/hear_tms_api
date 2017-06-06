from django.contrib import admin
from .models import Hear


# Register your models here.
@admin.register(Hear)
class HearAdmin(admin.ModelAdmin):
    list_display = ('id', 'song', 'file',)

    def has_add_permission(self, request):
        return False
