# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'home/index.html'
