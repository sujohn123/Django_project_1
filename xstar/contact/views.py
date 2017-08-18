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
		phone1 = form.cleaned_data['phone']
		email1 = form.cleaned_data['email']
		name1 = form.cleaned_data['name']
		if not(contactdetail.objects.filter(phone=phone1,name=name1)):
			c=contactdetail(phone=phone1,email=email1,name=name1)
			c.save()
			return HttpResponse('Success! Thank you for your message.')
		else:
			return HttpResponse('You are already registered, mate!!')
	
	return render(request, "xstars/basic.html",{'form': form})
