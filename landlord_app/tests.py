from django.test import TestCase, RequestFactory
import factory
from . import views
from django.contrib.auth.models import AnonymousUser
from factory.django import DjangoModelFactory
from django.shortcuts import render
from .models import User, Unit
from django.urls import reverse
import json


# Model Factories:


# User Factory doesn't work - see issue at https://github.com/FactoryBoy/factory_boy/issues/654
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

class UnitFactory(DjangoModelFactory):
    class Meta:
        model = Unit

    owner = factory.Iterator(User.objects.filter(username='user1'))


# Test Cases:

class RequestTestCase(TestCase):

    # https://blog.bitlabstudio.com/proper-unit-tests-for-your-django-views-b4a1730a922e
    def test_index(self):
        req = RequestFactory().get('/')
        resp = views.index(req)
        self.assertEqual(resp.status_code, 200)

    def test_landingpage(self):
        req = RequestFactory().get('/')
        req.user = UserFactory()
        resp = views.landing_page(req)
        self.assertEqual(resp.status_code, 200)

class Get_UnitsTestCase(TestCase):
    
    def setUp(self):

        # Create Users:
        user1 = UserFactory(username='user1')
        user2 = UserFactory(username='user2')

        # Create Units:
        unit1 = UnitFactory(zipcode='99999')
        unit2 = UnitFactory(zipcode='11111')

    def test_get_units_neg(self):
        user = User.objects.get(username='user2')
        req = RequestFactory().get('/')
        req.user = user
        resp = views.get_units(req)
        self.assertEqual(resp.content, b'[]')



# class authtestcase(TestCase):

#    def setUp(self):
#        u1 = UserFactory(username='test@test.com', password='12345')