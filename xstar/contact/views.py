# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from contact.models import contactdetail
from .forms import ContactForm

@csrf_exempt
def index(request):
    return render(request, 'xstars/forms.html')

def contact(request):
	form = ContactForm(request.POST or None)
	if request.POST and form.is_valid():
		name1 = form.cleaned_data['name']
        email1 = form.cleaned_data['email']
        phone1 = form.cleaned_data['phone']
	c=contactdetail(name=name1,email=email1,phone=phone1)
	c.save()
	
	return render(request, "xstars/basic.html",{'form': form})
