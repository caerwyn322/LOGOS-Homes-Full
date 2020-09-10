from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Designs


class DesignsAdmin(ImportExportActionModelAdmin):
    list_display = ('design_name', 'formatted_amount')
    list_filter = ['design_price']

    def formatted_amount(self, Designs):
        return '$%.2f' % Designs.design_price


admin.site.register(Designs, DesignsAdmin)