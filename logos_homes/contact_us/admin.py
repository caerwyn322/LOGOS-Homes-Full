from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Contacts
# Register your models here.

class ContactUsAdmin(ImportExportActionModelAdmin):
    list_display = ('name', 'email')


admin.site.register(Contacts, ContactUsAdmin)