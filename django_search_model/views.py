# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response('base.html')
