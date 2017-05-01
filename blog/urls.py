from django.conf.urls import url
from . import views


urlpatterns = [
    # post list
    url(r'^$', views.post_list, name='post_list'),
    # post detail
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # post update
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # post share
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    # create new post
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', 
        views.post_list, 
        name='post_list_by_tag'),
]
