# -*- encoding: utf-8 -*-

from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from forms import ContactForm

def contact(request):
    if request.POST:
      form = ContactForm(request.POST)
      if form.is_valid():
        emails = getattr(settings, 'CONTACT_EMAILS', [])
        send_mail('[usinasite] contact',
                  form.data['message'],
                  form.data['courriel'],
                  emails,
                  fail_silently=False)
        messages.add_message(request, messages.INFO, 'Le message a été envoyé. Merci.')
        return redirect('contact')
      else:
        messages.add_message(request, messages.ERROR, 'Il y a des erreurs dans le formulaire.')
        
    else:
      form = ContactForm()
      
    rc = RequestContext(request)
    c = {'form' : form}
    return render_to_response('contact/form.html', c, rc)
