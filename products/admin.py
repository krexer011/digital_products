from django.contrib import admin

from .models import Category,Product,File

from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enable', 'created_time']
    list_filter = ['is_enable', 'parent']
    search_fields = ['title']


class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file_type', 'file', 'is_enable']
    extra = 0


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'created_time']
    list_filter = ['is_enable']
    filter_horizontal = ['categories']
    search_fields = ['title']
    inlines = [FileInLineAdmin]

