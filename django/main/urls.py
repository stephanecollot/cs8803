from django.conf.urls import patterns, url

from main import views
from django.conf import settings

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^search/(?P<text>.*)$', views.search, name='search'),
  url(r'^document/(?P<id>\d+)$', views.openDocument, name='openDocument'),
)

urlpatterns += patterns('',
  url(r'^s/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': 'main/templates/s',
  }),
  url(r'^api/v1.0/document/(?P<id>\d+)[/]?$', views.DocumentViewSet.as_view(), name='document_viewset'),
  url(r'^api/v1.0/document[/]?$', views.DocumentViewSet.as_view(), name='document_viewset'),
  url(r'^api/v1.0/graph[/]?$', views.GraphViewSet.as_view(), name='graph_viewset'),
)
