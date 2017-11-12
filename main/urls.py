from django.conf.urls import url 
from . import views 

app_name = 'main'
urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^analyze/', views.analyze, name='analyaze'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^articles/(?P<article_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^articles/(?P<article_id>[0-9]+)/vote/$', views.vote, name='vote')
]