# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .serializers import RiskSerializer
# Create your views here.


class CreateRisk(ListCreateAPIView):
    serializer_class = RiskSerializer
