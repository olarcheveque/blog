# -*- encoding: utf-8 -*-

from django import forms

class ContactForm(forms.Form):
    courriel = forms.CharField(label=u"Courriel", max_length=255)
    nom = forms.CharField(label=u"Nom", max_length=255, required=False)
    message = forms.CharField(label=u"Message", max_length=255,
                          widget=forms.Textarea(attrs={'size':'60'}))
