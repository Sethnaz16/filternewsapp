from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fieldsets  = [
        (None, {'fields': ['article_url']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('article_url', 'pub_date', 'was_article_recommended')

admin.site.register(Article, ArticleAdmin)
