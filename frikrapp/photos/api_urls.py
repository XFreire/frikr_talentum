from django.conf.urls import patterns, url, include
from photos import api
from rest_framework.routers import DefaultRouter

# Creamos un router y registramos los viewsets

photo_router = DefaultRouter()
photo_router.register(r'photos', api.PhotoAPI)

urlpatterns = patterns('',

    # User API URLs
    url(r'^users/$', api.UserListAPI.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', api.UserDetailAPI.as_view()),

    # Photo API URLs
    url(r'^', include(photo_router.urls)),

)