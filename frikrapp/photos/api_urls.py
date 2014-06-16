from django.conf.urls import patterns, url, include
from photos import api
from rest_framework.routers import DefaultRouter

# Creamos un router y registramos los viewsets

photo_router = DefaultRouter()
photo_router.register(r'photos', api.PhotoAPI)

user_router = DefaultRouter()
user_router.register(r'users', api.UserAPI, base_name='user') # necesita base_name porque como no es un ModelViewSet, no sabe como nombrar internamente las URL

urlpatterns = patterns('',

    # User API URLs
    url(r'^', include(user_router.urls)),

    # Photo API URLs
    url(r'^', include(photo_router.urls)),

)