"""
URL configuration for PoliticalPartyManagement project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("i18n/", include("django.conf.urls.i18n")),

    path( "admin/", admin.site.urls),

    path("",include("cms.urls")),

    path("members/",include("members.urls")),

    path("admin-panel/",include("adminapp.urls")),

]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )