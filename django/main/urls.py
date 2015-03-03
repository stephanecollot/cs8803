from django.conf.urls import patterns, url

from main import views
from django.conf import settings

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
)

urlpatterns += patterns('',
  url(r'^s/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': 'main/templates/s',
  }),)