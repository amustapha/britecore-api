# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase


class RiskTests(APITestCase):

    def create_risk(self):
        data = {"name":"Test insurance","description":"Test insurance risks","field_set":[{"field":"Name"},{"field":"Email", "type": "email"}]}
        response = self.client.post(reverse('risk_list_or_create'), data)
        self.assertEqual(response.status_code, 201)

    def list_risks(self):
        response = self.client.get(reverse('risk_list_or_create'))
        self.assertEqual(response.status_code, 200)

    def view_risk(self):
        response = self.client.get(reverse('risk_detail', 1))
        self.assertEqual(response.status_code, 201)
