from django.db import models
from datetime import date

# TO-DO: Add-in image fields

class User(models.Model):
    username = models.EmailField(max_length=254)
    password = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    company = models.CharField(max_length=80)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    zipcode = models.PositiveIntegerField()
    units = models.ForeignKey(
        'Units',
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
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    tenants = models.ForeignKey(
        'Tenants',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


class Tenant(models.Model):
    tenant_number = models.PositiveIntegerField()
    tenant_first = models.CharField(max_length=40)
    tenant_last = models.CharField(max_length=40)
    tenant_ssn = models.PositiveIntegerField()
    tenant_email = models.EmailField(max_length=254)
    tenant_start = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    tenant_end = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    leases = models.ForeignKey(
        'Leases',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    tenant_payments = models.ForeignKey(
        'Tenant_Payments',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    evict_notices = models.ForeignKey(
        'Evict_Notices',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


class Lease(models.Model):
    rent_amount = models.DecimalField(max_digits=9, decimal_places=2)
    secdep_amount = models.DecimalField(max_digits=9, decimal_places=2)
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
