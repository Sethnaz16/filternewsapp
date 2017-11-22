from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import main.views
import home.views

# Examples:
# url(r'^$', 'filternewsapp.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^', include('main.urls')),
   # url(r'^main/', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
