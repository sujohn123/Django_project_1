# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class contactdetail(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
	phone = models.CharField(max_length=20)