from django.conf.urls import patterns, url
from photos import api

urlpatterns = patterns('',

    # User API URLs
    url(r'^users/$', api.UserListAPI.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', api.UserDetailAPI.as_view()),

    # Photo API URLs
    url(r'^photos/$', api.PhotoListAPI.as_view()),
    url(r'^photos/(?P<pk>[0-9]+)$', api.PhotoDetailAPI.as_view()),
    url(r'^photos/upload$', api.PhotoUploadAPI.as_view()),

)