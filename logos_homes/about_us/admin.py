from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import TeamMembers
# Register your models here.


class AboutUsAdmin(ImportExportActionModelAdmin):
    list_display = ('member_name', 'member_position')


admin.site.register(TeamMembers, AboutUsAdmin)