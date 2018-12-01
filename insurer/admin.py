# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Field, Risk, SubmissionSet, SubmissionValue

# Register your models here.
for model in [Field, Risk, SubmissionValue, SubmissionSet]:
    admin.site.register(model)
