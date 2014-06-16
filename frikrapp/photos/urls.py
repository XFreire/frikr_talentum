from django.conf.urls import patterns, url
from photos import views

# Web URLS
urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view()),
    url(r'^photos/$', views.PhotoListView.as_view()),
    url(r'^photos/(?P<pk>[0-9]+)$', views.PhotoDetailView.as_view()),
    url(r'^login$', views.UserLoginView.as_view()),
    url(r'^logout$', views.UserLogoutView.as_view()),
    url(r'^profile$', views.UserProfileView.as_view()),
    url(r'^create$', 'photos.views.create_photo'),
)