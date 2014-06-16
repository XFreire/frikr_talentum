from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

from photos import urls as photo_web_urls
from photos import api_urls as photo_api_urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Web URLS
    url(r'', include(photo_web_urls)),

    # API URLs
    url(r'^api/1.0/', include(photo_api_urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)