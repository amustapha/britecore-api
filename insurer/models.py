# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.text import slugify


class Risk(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()


class Field(models.Model):
    risk = models.ForeignKey(Risk)
    field = models.CharField(max_length=255)
    key = models.SlugField(max_length=255)

    def save(self, **kwargs):
        self.key = "{}-{}".format(Field.objects.count() + 1, slugify(self.field))
        super(Field, self).save(**kwargs)