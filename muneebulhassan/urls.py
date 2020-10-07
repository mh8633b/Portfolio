from django.conf import settings
from django.conf.urls import url
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = [
    path("", views.index, name="index.html"),
    path("add/", views.index, name="index.html"),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
