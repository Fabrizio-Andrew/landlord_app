from django.db import models

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
    zipcode = models.PositiveIntegerField(max_value=99999)
    units = models.ForeignKey(
        'Units',
        on_delete=models.CASCADE
    )
    reg_ovrhd_expenses = models.ForeignKey(
        'Reg_Ovrhd_Expenses',
        on_delete=models.CASCADE
    )
    ovrhd_expense_pmts = models.ForeignKey(
        'Ovrhd_Expense_Pmts',
        on_delete=models.CASCADE
    )



class Units(models.Model):
    nickname = models.CharField(max_length=40)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    zipcode = models.PositiveIntegerField(max_value=99999)
    bedrooms = models.PositiveIntegerField(max_value=20)
    bathrooms = models.PositiveIntegerField(max_value=20)
    tenants = models.ForeignKey(
        'Tenants',
        on_delete=models.CASCADE
    )
    reg_unit_expenses = models.ForeignKey(
        'Reg_Unit_Expenses',
        on_delete=models.CASCADE
    )
    unit_expense_pmts = models.ForeignKey(
        'Unit_Expense_Pmts',
        on_delete=models.CASCADE
    )
    oth_unit_income = models.ForeignKey(
        'Oth_Unit_Income',
        on_delete=models.CASCADE
    )

class Reg_Ovrhd_Expenses(models.Model):
    mortgage = models.DecimalField(max_digits=9, decimal_places=2)
    insurance = models.DecimalField(max_digits=9, decimal_places=2)
    taxes = models.DecimalField(max_digits=9, decimal_places=2)
    hoa = models.DecimalField(max_digits=9, decimal_places=2)
    electric = models.DecimalField(max_digits=9, decimal_places=2)
    water = models.DecimalField(max_digits=9, decimal_places=2)
    garbage = models.DecimalField(max_digits=9, decimal_places=2)
    other_name = models.CharField(max_length=20)
    other_amount = models.DecimalField(max_digits=9, decimal_places=2)

class Ovrhd_Expense_Pmts(models.Model):
    payer_first = models.CharField(max_length=40)
    payer_last = models.CharField(max_length=40)
    payer_company = models.CharField(max_length=80)
    payer_biz = models.BooleanField()
    payer_email = models.EmailField(max_length=254)
    pay_method = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date_paid = models.DateField(auto_now=False, auto_now_add=False)
    reason = models.CharField(max_length=40)
    rtn_number = models.PositiveIntegerField()
    acct_number = models.PositiveIntegerField()
    acct_type = models.CharField(max_length=1)
    check_num = models.PositiveIntegerField(max_value=9999)
#    check_img = ImageField()
    cc_num = models.PositiveIntegerField()
    cc_exp_month = models.PositiveIntegerField(max_value=12)
    cc_exp_year = models.PositiveIntegerField(max_value=2040)
    cc_vercode = models.PositiveIntegerField()

class Tenants(models.Model):
    tenant_number = models.PositiveIntegerField(max_value=4)
    tenant1_first = models.CharField(max_length=40)
    tenant1_last = models.CharField(max_length=40)
    tenant1_ssn = models.PositiveIntegerField(max_value=999999999)
    tenant1_email = models.EmailField(max_length=254)
    tenant2_first = models.CharField(max_length=40)
    tenant2_last = models.CharField(max_length=40)
    tenant2_ssn = models.PositiveIntegerField(max_value=999999999)
    tenant2_email = models.EmailField(max_length=254)
    tenant3_first = models.CharField(max_length=40)
    tenant3_last = models.CharField(max_length=40)
    tenant3_ssn = models.PositiveIntegerField(max_value=999999999)
    tenant3_email = models.EmailField(max_length=254)
    tenant4_first = models.CharField(max_length=40)
    tenant4_last = models.CharField(max_length=40)
    tenant4_ssn = models.PositiveIntegerField(max_value=999999999)
    tenant4_email = models.EmailField(max_length=254)
    pets = models.JSONField(encoder=None, decoder=None)
    leases = models.ForeignKey(
        'Leases',
        on_delete=models.CASCADE
    )
    oth_docs = models.ForeignKey(
        'Oth_Docs',
        on_delete=models.CASCADE
    )
    tenant_payments = models.ForeignKey(
        'Tenant_Payments',
        on_delete=models.CASCADE
    )
    evict_notices = models.ForeignKey(
        'Evict_Notices',
        on_delete=models.CASCADE
    )
