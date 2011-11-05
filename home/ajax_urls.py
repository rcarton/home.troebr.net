from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    
    url(r'^add/message$', 'home.common.ajax_views.add_message', name='add_message'),
    
)
