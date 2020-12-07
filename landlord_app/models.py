from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

# All of these fields are optional to make Factory Boy happy
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
#            ten = {
#                "id": tenant.pk,
#                "first_name": tenant.tenant_first,
#                "last_name": tenant.tenant_last,
#                }
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
#    tenant_start = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
#    tenant_end = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    unit = models.ForeignKey(
        'Unit',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    lease = models.ForeignKey(
        'Lease',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"<{self.pk}: {self.tenant_first} {self.tenant_last}>"

    def serialize(self):
#        l = self.lease.serialize()
        return {
            "id": self.pk,
            "tenant_first": self.tenant_first,
            "tenant_last": self.tenant_last,
            "tenant_email": self.tenant_email,
#            "tenant_start": self.tenant_start,
#            "tenant_end": self.tenant_end,
#            "lease": l
        }


class Lease(models.Model):
    rent_amount = models.DecimalField(max_digits=9, decimal_places=2)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    date_signed = models.DateField(auto_now=False, auto_now_add=False)
    electric_ind = models.BooleanField(null=True, blank=True)
    water_ind = models.BooleanField(null=True, blank=True)
    garbage_ind = models.BooleanField(null=True, blank=True)
#    lease_img = ImageField()
    petfee_amt = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    petfee_type = models.CharField(max_length=1, null=True, blank=True)
    othfee_name = models.CharField(max_length=40, null=True, blank=True)
    othfee_amt = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    rollover = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return f"<{self.pk}: {self.rent_amount}/month {self.start_date} to {self.end_date}>"

    def serialize(self):
        return {
            "id": self.pk,
            "rent_amount": self.rent_amount,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "date_signed": self.date_signed,
            "electric_ind": self.electric_ind,
            "water_ind": self.water_ind,
            "garbage_ind": self.garbage_ind,
        }


#class Tenant_Payment(models.Model):
#    payer_first = models.CharField(max_length=40)
#    payer_last = models.CharField(max_length=40)
#    payer_company = models.CharField(max_length=80)
#    payer_bizind = models.BooleanField()
#    payer_email = models.EmailField(max_length=254)
#    pay_method = models.CharField(max_length=20)
#    amount = models.DecimalField(max_digits=9, decimal_places=2)
#    date_paid = models.DateField(auto_now=False, auto_now_add=False)
#    reason = models.CharField(max_length=40)
#    rtn_number = models.PositiveIntegerField()
#    acct_number = models.PositiveIntegerField()
#    acct_type = models.CharField(max_length=1)
#    check_num = models.PositiveIntegerField()
#    check_img = ImageField()
#    cc_num = models.PositiveIntegerField()
#    cc_exp_month = models.PositiveIntegerField()
#    cc_exp_year = models.PositiveIntegerField()
#    cc_vercode = models.PositiveIntegerField()

#class Evict_Notice(models.Model):
#    notice_type = models.CharField(max_length=40)
#    date_sent = models.DateField(auto_now=False, auto_now_add=False)
#    delivery_method = models.CharField(max_length=40)

