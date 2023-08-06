from django.contrib import admin
from djangorestfilemanager.models import File


# Register your models here.

class FileAdmin(admin.ModelAdmin):
    search_fields = ['uuid', 'name', 'user_name', 'creation_date', 'last_mod_date']
    list_display = ['uuid', 'name', 'user_name', 'creation_date', 'last_mod_date', 'origin', 'type', 'permission',
                    'share']
    list_display_links = ['uuid', ]
    ordering = ['uuid', 'name', 'user_name', 'creation_date', 'last_mod_date', 'origin', 'type', 'permission',
                'share']
    list_filter = ['origin', 'type', 'share']


admin.site.register(File, FileAdmin)
