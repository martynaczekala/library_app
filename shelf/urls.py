from django.conf.urls import patterns, include, url

from shelf import views

urlpatterns = patterns('',
    url(r'^authors/$', views.AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author-detail')
    )