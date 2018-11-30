# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Field, Risk

# Register your models here.
admin.site.register(Field)
admin.site.register(Risk)
