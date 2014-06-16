from django.conf.urls import patterns, url
from photos import views

# Web URLS
urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^photos/$', views.PhotoListView.as_view(), name='photo_list'),
    url(r'^photos/(?P<pk>[0-9]+)$', views.PhotoDetailView.as_view(), name='photo_detail'),
    url(r'^login$', views.UserLoginView.as_view(), name='user_login'),
    url(r'^logout$', views.UserLogoutView.as_view(), name='user_logout'),
    url(r'^profile$', views.UserProfileView.as_view(), name='user_profile'),
    url(r'^create$', 'photos.views.create_photo', name='new_photo'),
)