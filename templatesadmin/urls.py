from django.conf.urls import url
from django.conf.urls import patterns

urlpatterns = patterns('',
    url(r'^$', 'templatesadmin.views.listing', name='templatesadmin-overview'),
    url(r'^edit(?P<path>.*)/$', 'templatesadmin.views.modify', name='templatesadmin-edit'),
)
