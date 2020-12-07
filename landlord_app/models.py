from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class User(AbstractUser):
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    zipcode = models.PositiveIntegerField()

    def __str__(self):
        return f"<{self.pk}: {self.username}>"

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "address_line1": self.address_line1,
            "address_line2": self.address_line2,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode
        }


class State(models.Model):
    abbrev = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=20)
    failtopay = models.BooleanField()
    failtopaydays = models.IntegerField()
    failtopaynotice = models.CharField(max_length=20)
    failtopaynoticedays = models.IntegerField()
    posethreat = models.BooleanField()
    posethreatnotice = models.CharField(max_length=20)
    posethreatnoticedays = models.IntegerField()
    violatelease = models.BooleanField()
    violateleasenotice = models.CharField(max_length=20)
    violateleasenoticedays = models.IntegerField()
    mtom = models.BooleanField()
    mtomnotice = models.CharField(max_length=20)
    mtomnoticedays = models.IntegerField()

    def __str__(self):
        return f"<{self.pk}>"

    def serialize(self):
        return {
            "id": self.abbrev,
            "name": self.name,
            "failtopay": self.failtopay,
            "failtopaydays": self.failtopaydays,
            "failtopaynotice": self.failtopaynotice,
            "failtopaynoticedays": self.failtopaynoticedays,
            "posethreat": self.posethreat,
            "posethreatnotice": self.posethreatnotice,
            "posethreatnoticedays": self.posethreatnoticedays,
            "violatelease": self.violatelease,
            "violateleasenotice": self.violateleasenotice,
            "violateleasenoticedays": self.violateleasenoticedays,
            "mtom": self.mtom,
            "mtomnotice": self.mtomnotice,
            "mtomnoticedays": self.mtomnoticedays
        }


class Unit(models.Model):
    nickname = models.CharField(max_length=40)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=40)
    zipcode = models.PositiveIntegerField()
    state = models.ForeignKey(
        'State',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    owner = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    def __str__(self):
        return f"<{self.pk}: owned by {self.owner}>"

    def serialize(self):
        tenantlist = []
        for tenant in Tenant.objects.filter(unit=self):
            ten = tenant.serialize()
            tenantlist.append(ten)
        return {
            "id": self.id,
            "nickname": self.nickname,
            "address_line1": self.address_line1,
            "address_line2": self.address_line2,
            "city": self.city,
            "state": self.state.pk,
            "zipcode": self.zipcode,
            "owner": self.owner.id,
            "tenants": tenantlist
        }


class Tenant(models.Model):
    tenant_first = models.CharField(max_length=40)
    tenant_last = models.CharField(max_length=40)
    tenant_email = models.EmailField(max_length=254)
    unit = models.ForeignKey(
        'Unit',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    def __str__(self):
        return f"<{self.pk}: {self.tenant_first} {self.tenant_last}>"

    def serialize(self):
        return {
            "id": self.pk,
            "tenant_first": self.tenant_first,
            "tenant_last": self.tenant_last,
            "tenant_email": self.tenant_email,
        }
