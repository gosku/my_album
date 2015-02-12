from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  # Urls de Django-allauth
  url(r'^accounts/', include('allauth.urls')),
  url(r'^album/', include('album.urls')),
  url(r'^$', include('album.urls')),
  # Admin de Django
  url(r'^admin/', include(admin.site.urls)),
)
