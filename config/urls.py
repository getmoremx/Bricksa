#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as error_views

from bricksa.apps.landing import urls as landing_urls
from bricksa.apps.projects import urls as project_urls
from bricksa.apps.newsletter import urls as newsletter_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Custom urls
    url(r'', include(landing_urls, namespace='landing')),
    url(r'', include(project_urls, namespace='projects')),
    url(r'', include(newsletter_urls, namespace='newsletter'))
]

if settings.DEBUG:
    import debug_toolbar
    # This allows the error pages to be debugged during development, visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^400/$', error_views.bad_request, kwargs={
            'exception': Exception("Bad Request!")}),
        url(r'^403/$', error_views.permission_denied, kwargs={
            'exception': Exception("Permission Denied")}),
        url(r'^404/$', error_views.page_not_found, kwargs={
            'exception': Exception("Page not Found")}),
        url(r'^500/$', error_views.server_error),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
