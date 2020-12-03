from django.test import TestCase, RequestFactory
import factory
from . import views
from django.contrib.auth.models import AnonymousUser
from factory.django import DjangoModelFactory
from django.shortcuts import render
from .models import User, Unit, State
from django.urls import reverse
import json


###################################### MODEL FACTORIES ######################################


# User Factory doesn't work - see issue at https://github.com/FactoryBoy/factory_boy/issues/654
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('ascii_safe_email')
    address_line1 = factory.Faker('street_address')
    city = factory.Faker('city')
    state = factory.Faker('state')
    zipcode = factory.Faker('postcode')


class UnitFactory(DjangoModelFactory):
    class Meta:
        model = Unit
        
    owner = factory.Iterator(User.objects.filter(username='user1'))
    nickname = factory.Faker('first_name')
    address_line1 = factory.Faker('street_address')
    city = factory.Faker('city')
    state = factory.Iterator(State.objects.filter(pk='MD'))
    zipcode = factory.Faker('postcode')

class StateFactory(DjangoModelFactory):
    class Meta:
        model = State

    abbrev = 'MD'
    name = 'Maryland'
    failtopay = True
    failtopaydays = 1
    failtopaynotice = 'Letter'
    failtopaynoticedays = 30
    posethreat = True
    posethreatnotice = 'Letter'
    posethreatnoticedays = 14
    violatelease = True
    violateleasenotice = 'Letter'
    violateleasenoticedays = 30
    mtom = True
    mtomnotice = 'Letter'
    mtomnoticedays = 30



###################################### TEST CASES ######################################

class StateRulesTestCase(TestCase):

    # This test case is failing for some reason

    def setup(self):

        # Create State
        teststate = StateFactory(abbrev='MD').pk
        print(teststate)

    def test_staterules(self):

        req = RequestFactory()
        state = 'md'
        resp = views.state_rules(req, state)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.content["name"], 'Maryland')



class RequestTestCase(TestCase):

    def setup(self):

        # Create State
        teststate = StateFactory()

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
    
    def test_evictiontree(self):
        req = RequestFactory().get('/evictiontree')
        resp = views.eviction_tree(req)
        self.assertEqual(resp.status_code, 200)


class Get_UnitsTestCase(TestCase):
    
    def setUp(self):

        # Create State
        teststate = StateFactory()

        # Create Users:
        user1 = UserFactory(username='user1', zipcode='11111')
        user2 = UserFactory(username='user2', zipcode='12345')

        # Create Units:
        unit1 = UnitFactory(zipcode='11111')
        unit2 = UnitFactory(zipcode='22222')

    def test_get_units(self):
        user = User.objects.get(username='user1')
        req = RequestFactory().get('/')
        req.user = user
        resp = views.get_units(req)
        jsonresp = json.loads(resp.content)
        unit1 = jsonresp[0]
        unit2 = jsonresp[1]

        # Validate unit1
        self.assertEqual(unit1["id"], 1)
        self.assertEqual(unit1["owner"], 1)
        self.assertEqual(type(unit1["nickname"]), str)
        self.assertEqual(type(unit1["address_line1"]), str)
        self.assertEqual(unit1["address_line2"], None)
        self.assertEqual(type(unit1["city"]), str)
        self.assertEqual(type(unit1["state"]), str)
        self.assertEqual(unit1["zipcode"], 11111)

        # Validate unit2
        self.assertEqual(unit2["id"], 2)
        self.assertEqual(unit2["owner"], 1)
        self.assertEqual(type(unit2["nickname"]), str)
        self.assertEqual(type(unit2["address_line1"]), str)
        self.assertEqual(unit2["address_line2"], None)
        self.assertEqual(type(unit2["city"]), str)
        self.assertEqual(type(unit2["state"]), str)
        self.assertEqual(unit2["zipcode"], 22222)

    
    def test_get_units_neg(self):
        user = User.objects.get(username='user2')
        req = RequestFactory().get('/')
        req.user = user
        resp = views.get_units(req)
        self.assertEqual(json.loads(resp.content), [])

    



# class authtestcase(TestCase):

#    def setUp(self):
#        u1 = UserFactory(username='test@test.com', password='12345')