# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView

from insurer.models import Risk
from .serializers import RiskSerializer, SubmissionSerializer


# Create your views here.


class ListRiskView(ListCreateAPIView):
    serializer_class = RiskSerializer
    queryset = Risk.objects.all()


class RiskDetailView(RetrieveAPIView):
    serializer_class = RiskSerializer
    queryset = Risk.objects.all()


class SubmissionView(CreateAPIView):
    serializer_class = SubmissionSerializer

