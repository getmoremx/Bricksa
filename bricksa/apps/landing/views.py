#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.template.response import TemplateResponse
from django.views.generic import TemplateView, View

from bricksa.apps.projects.models import ProjectBanner


class HomepageView(View):
    def get(self, request):
        banners = ProjectBanner.objects.all()
        ctx = {
            'banners': banners
        }
        return TemplateResponse(request, 'landing/index.html', ctx)

class ServicesView(TemplateView):
    template_name = 'landing/services.html'

