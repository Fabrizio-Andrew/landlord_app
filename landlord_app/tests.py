from django.test import TestCase, RequestFactory
import factory
from . import views
from django.contrib.auth.models import AnonymousUser
from factory.django import DjangoModelFactory
from django.shortcuts import render
from .models import User
from django.urls import reverse


# Model Factories:

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User


# Test Cases:

class RequestTestCase(TestCase):

    # https://blog.bitlabstudio.com/proper-unit-tests-for-your-django-views-b4a1730a922e
    def test_index(self):
        req = RequestFactory().get('/')
        resp = views.index(req)
        self.assertEqual(resp.status_code, 200)

    def test_landingpage(self):
        req = RequestFactory().get('/')
        resp = views.landing_page(req)
        self.assertEqual(resp.status_code, 200)


# class authtestcase(TestCase):

#    def setUp(self):
#        u1 = UserFactory(username='test@test.com', password='12345')