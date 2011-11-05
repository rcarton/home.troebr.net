from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.common.views.home', name='home'),
    url(r'^p/(?P<place_name>.+)$', 'home.common.views.home', name='home_with_place'),
    url(r'^hello$', 'home.common.views.hello', name='hello'),
    url(r'^logout$', 'home.common.views.disconnect', name='logout'),
    url(r'^ajax/', include('home.ajax_urls')),
    
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
