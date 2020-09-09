from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Designs


class DesignsAdmin(ImportExportActionModelAdmin):
    list_display = ('design_name', 'design_price')


admin.site.register(Designs, DesignsAdmin)