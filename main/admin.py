from django.contrib import admin
from .models import Article, Label, UnreliableSource
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ArticleAdmin(admin.ModelAdmin):
    fieldsets  = [
        (None, {'fields': ['article_url']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('article_url', 'pub_date', 'was_article_recommended')

class LabelResources(resources.ModelResource):
    class Meta:
        model = Label

class LabelAdmin(ImportExportModelAdmin):
    resource_class = LabelResources
    fieldsets = [
        (None, {'fields': ['label', 'description']}),
    ]
    list_display = ('label', 'description')

class UnreliableResources(resources.ModelResource):
    class Meta:
        model = UnreliableSource

class UnreliableAdmin(ImportExportModelAdmin):
    resource_class = UnreliableResources
    fieldsets = [
        (None, {'fields': ['source', 'label']}),
    ]
    list_display = ('source', 'label')

admin.site.register(Article, ArticleAdmin)

admin.site.register(Label, LabelAdmin)

admin.site.register(UnreliableSource, UnreliableAdmin)