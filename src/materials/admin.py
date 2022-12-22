from django.contrib import admin

from .models import Catalog, Document


class DocumentInline(admin.TabularInline):
    model = Document


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id',)
    fields = ('name',)
    search_fields = ('name',)
    inlines = [DocumentInline]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'catalog', 'is_private', 'disk_path',)
    list_display_links = ('id', 'name',)
    list_editable = ('is_private',)
    list_filter = ('catalog', 'is_private')
    fields = ('catalog', 'name', 'is_private', 'disk_path',)
    search_fields = ('name',)


admin.site.site_header = 'Администрирование Корпоративной базы знаний'
