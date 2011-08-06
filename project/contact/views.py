# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def contact(request):
    rc = RequestContext(request)
    c = {}
    return render_to_response('contact/form.html', c, rc)
