from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class User(AbstractUser):
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    zipcode = models.PositiveIntegerField()
    units = models.ForeignKey(
        'Unit',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


class Unit(models.Model):
    nickname = models.CharField(max_length=40)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    zipcode = models.PositiveIntegerField()
    tenants = models.ForeignKey(
        'Tenant',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


class Tenant(models.Model):
    tenant_first = models.CharField(max_length=40)
    tenant_last = models.CharField(max_length=40)
    tenant_email = models.EmailField(max_length=254)
    tenant_start = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    tenant_end = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    lease = models.ForeignKey(
        'Lease',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    tenant_payments = models.ForeignKey(
        'Tenant_Payment',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    evict_notices = models.ForeignKey(
        'Evict_Notice',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


class Lease(models.Model):
    rent_amount = models.DecimalField(max_digits=9, decimal_places=2)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    date_signed = models.DateField(auto_now=False, auto_now_add=False)
    electric_ind = models.BooleanField()
    water_ind = models.BooleanField()
    garbage_ind = models.BooleanField()
#    lease_img = ImageField()
    petfee_amt = models.DecimalField(max_digits=9, decimal_places=2)
    petfee_type = models.CharField(max_length=1)
    othfee_name = models.CharField(max_length=40)
    othfee_amt = models.DecimalField(max_digits=9, decimal_places=2)
    rollover = models.CharField(max_length=1)


class Tenant_Payment(models.Model):
    payer_first = models.CharField(max_length=40)
    payer_last = models.CharField(max_length=40)
    payer_company = models.CharField(max_length=80)
    payer_bizind = models.BooleanField()
    payer_email = models.EmailField(max_length=254)
    pay_method = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date_paid = models.DateField(auto_now=False, auto_now_add=False)
    reason = models.CharField(max_length=40)
    rtn_number = models.PositiveIntegerField()
    acct_number = models.PositiveIntegerField()
    acct_type = models.CharField(max_length=1)
    check_num = models.PositiveIntegerField()
#    check_img = ImageField()
    cc_num = models.PositiveIntegerField()
    cc_exp_month = models.PositiveIntegerField()
    cc_exp_year = models.PositiveIntegerField()
    cc_vercode = models.PositiveIntegerField()

class Evict_Notice(models.Model):
    notice_type = models.CharField(max_length=40)
    date_sent = models.DateField(auto_now=False, auto_now_add=False)
    delivery_method = models.CharField(max_length=40)
