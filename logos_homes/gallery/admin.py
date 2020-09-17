from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *
# Register your models here.


class GalleryImagesAdmin(admin.ModelAdmin):
    pass


class ProjectImagesInline(admin.StackedInline):
    model = ProjectImages
    max_num = 5
    extra = 0


class GalleryAdmin(ImportExportActionModelAdmin):
    list_display = ('project_name', 'project_status')
    inlines = [ProjectImagesInline]


admin.site.register(ProjectImages, GalleryImagesAdmin)
admin.site.register(Projects, GalleryAdmin)