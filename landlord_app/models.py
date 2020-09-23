from django.db import models
from datetime import date

# TO-DO: Add-in image fields

class Users(models.Model):
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
    reg_ovrhd_expenses = models.ForeignKey(
        'Reg_Ovrhd_Expenses',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    ovrhd_expense_pmts = models.ForeignKey(
        'Ovrhd_Expense_Pmts',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )



class Units(models.Model):
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
    reg_unit_expenses = models.ForeignKey(
        'Reg_Unit_Expenses',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    unit_expense_pmts = models.ForeignKey(
        'Unit_Expense_Pmts',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    oth_unit_income = models.ForeignKey(
        'Oth_Unit_Income',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

class Reg_Ovrhd_Expenses(models.Model):
    other_name = models.CharField(max_length=20)
    other_amount = models.DecimalField(max_digits=9, decimal_places=2)

class Ovrhd_Expense_Pmts(models.Model):
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

class Tenants(models.Model):
    tenant_number = models.PositiveIntegerField()
    tenant1_first = models.CharField(max_length=40)
    tenant1_last = models.CharField(max_length=40)
    tenant1_ssn = models.PositiveIntegerField()
    tenant1_email = models.EmailField(max_length=254)
    tenant1_start = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    tenant1_end = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    tenant2_first = models.CharField(max_length=40)
    tenant2_last = models.CharField(max_length=40)
    tenant2_ssn = models.PositiveIntegerField()
    tenant2_email = models.EmailField(max_length=254)
    tenant2_start = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    tenant2_end = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    tenant3_first = models.CharField(max_length=40)
    tenant3_last = models.CharField(max_length=40)
    tenant3_ssn = models.PositiveIntegerField()
    tenant3_email = models.EmailField(max_length=254)
    tenant3_start = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    tenant3_end = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    tenant4_first = models.CharField(max_length=40)
    tenant4_last = models.CharField(max_length=40)
    tenant4_ssn = models.PositiveIntegerField()
    tenant4_email = models.EmailField(max_length=254)
    tenant4_start = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    tenant4_end = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    pets = models.JSONField(encoder=None, decoder=None)
    leases = models.ForeignKey(
        'Leases',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    oth_docs = models.ForeignKey(
        'Oth_Docs',
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

class Reg_Unit_Expenses(models.Model):
    mortgage = models.DecimalField(max_digits=9, decimal_places=2)
    insurance = models.DecimalField(max_digits=9, decimal_places=2)
    taxes = models.DecimalField(max_digits=9, decimal_places=2)
    hoa = models.DecimalField(max_digits=9, decimal_places=2)
    electric = models.DecimalField(max_digits=9, decimal_places=2)
    water = models.DecimalField(max_digits=9, decimal_places=2)
    garbage = models.DecimalField(max_digits=9, decimal_places=2)
    other_name = models.CharField(max_length=20)
    other_amount = models.DecimalField(max_digits=9, decimal_places=2)

class Unit_Expense_Pmts(models.Model):
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

class Oth_Unit_Income(models.Model):
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

class Leases(models.Model):
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

class Oth_Docs(models.Model):
    doc_type = models.CharField(max_length=40)
    date_signed = models.DateField(auto_now=False, auto_now_add=False)
#    doc_img = ImageField()

class Tenant_Payments(models.Model):
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

class Evict_Notices(models.Model):
    notice_type = models.CharField(max_length=40)
    date_sent = models.DateField(auto_now=False, auto_now_add=False)
    delivery_method = models.CharField(max_length=40)
