# Generated by Django 3.1.1 on 2020-09-22 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landlord_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evict_Notices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_type', models.CharField(max_length=40)),
                ('date_sent', models.DateField()),
                ('delivery_method', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Leases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('secdep_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('date_signed', models.DateField()),
                ('electric_ind', models.BooleanField()),
                ('water_ind', models.BooleanField()),
                ('garbage_ind', models.BooleanField()),
                ('petfee_amt', models.DecimalField(decimal_places=2, max_digits=9)),
                ('petfee_type', models.CharField(max_length=1)),
                ('othfee_name', models.CharField(max_length=40)),
                ('othfee_amt', models.DecimalField(decimal_places=2, max_digits=9)),
                ('rollover', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Oth_Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(max_length=40)),
                ('date_signed', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Oth_Unit_Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer_first', models.CharField(max_length=40)),
                ('payer_last', models.CharField(max_length=40)),
                ('payer_company', models.CharField(max_length=80)),
                ('payer_bizind', models.BooleanField()),
                ('payer_email', models.EmailField(max_length=254)),
                ('pay_method', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date_paid', models.DateField()),
                ('reason', models.CharField(max_length=40)),
                ('rtn_number', models.PositiveIntegerField()),
                ('acct_number', models.PositiveIntegerField()),
                ('acct_type', models.CharField(max_length=1)),
                ('check_num', models.PositiveIntegerField()),
                ('cc_num', models.PositiveIntegerField()),
                ('cc_exp_month', models.PositiveIntegerField()),
                ('cc_exp_year', models.PositiveIntegerField()),
                ('cc_vercode', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ovrhd_Expense_Pmts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer_first', models.CharField(max_length=40)),
                ('payer_last', models.CharField(max_length=40)),
                ('payer_company', models.CharField(max_length=80)),
                ('payer_bizind', models.BooleanField()),
                ('payer_email', models.EmailField(max_length=254)),
                ('pay_method', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date_paid', models.DateField()),
                ('reason', models.CharField(max_length=40)),
                ('rtn_number', models.PositiveIntegerField()),
                ('acct_number', models.PositiveIntegerField()),
                ('acct_type', models.CharField(max_length=1)),
                ('check_num', models.PositiveIntegerField()),
                ('cc_num', models.PositiveIntegerField()),
                ('cc_exp_month', models.PositiveIntegerField()),
                ('cc_exp_year', models.PositiveIntegerField()),
                ('cc_vercode', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reg_Ovrhd_Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_name', models.CharField(max_length=20)),
                ('other_amount', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Reg_Unit_Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mortgage', models.DecimalField(decimal_places=2, max_digits=9)),
                ('insurance', models.DecimalField(decimal_places=2, max_digits=9)),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=9)),
                ('hoa', models.DecimalField(decimal_places=2, max_digits=9)),
                ('electric', models.DecimalField(decimal_places=2, max_digits=9)),
                ('water', models.DecimalField(decimal_places=2, max_digits=9)),
                ('garbage', models.DecimalField(decimal_places=2, max_digits=9)),
                ('other_name', models.CharField(max_length=20)),
                ('other_amount', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant_Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer_first', models.CharField(max_length=40)),
                ('payer_last', models.CharField(max_length=40)),
                ('payer_company', models.CharField(max_length=80)),
                ('payer_bizind', models.BooleanField()),
                ('payer_email', models.EmailField(max_length=254)),
                ('pay_method', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date_paid', models.DateField()),
                ('reason', models.CharField(max_length=40)),
                ('rtn_number', models.PositiveIntegerField()),
                ('acct_number', models.PositiveIntegerField()),
                ('acct_type', models.CharField(max_length=1)),
                ('check_num', models.PositiveIntegerField()),
                ('cc_num', models.PositiveIntegerField()),
                ('cc_exp_month', models.PositiveIntegerField()),
                ('cc_exp_year', models.PositiveIntegerField()),
                ('cc_vercode', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tenants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_number', models.PositiveIntegerField()),
                ('tenant1_first', models.CharField(max_length=40)),
                ('tenant1_last', models.CharField(max_length=40)),
                ('tenant1_ssn', models.PositiveIntegerField()),
                ('tenant1_email', models.EmailField(max_length=254)),
                ('tenant2_first', models.CharField(max_length=40)),
                ('tenant2_last', models.CharField(max_length=40)),
                ('tenant2_ssn', models.PositiveIntegerField()),
                ('tenant2_email', models.EmailField(max_length=254)),
                ('tenant3_first', models.CharField(max_length=40)),
                ('tenant3_last', models.CharField(max_length=40)),
                ('tenant3_ssn', models.PositiveIntegerField()),
                ('tenant3_email', models.EmailField(max_length=254)),
                ('tenant4_first', models.CharField(max_length=40)),
                ('tenant4_last', models.CharField(max_length=40)),
                ('tenant4_ssn', models.PositiveIntegerField()),
                ('tenant4_email', models.EmailField(max_length=254)),
                ('pets', models.JSONField()),
                ('evict_notices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.evict_notices')),
                ('leases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.leases')),
                ('oth_docs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.oth_docs')),
                ('tenant_payments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.tenant_payments')),
            ],
        ),
        migrations.CreateModel(
            name='Unit_Expense_Pmts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer_first', models.CharField(max_length=40)),
                ('payer_last', models.CharField(max_length=40)),
                ('payer_company', models.CharField(max_length=80)),
                ('payer_bizind', models.BooleanField()),
                ('payer_email', models.EmailField(max_length=254)),
                ('pay_method', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('date_paid', models.DateField()),
                ('reason', models.CharField(max_length=40)),
                ('rtn_number', models.PositiveIntegerField()),
                ('acct_number', models.PositiveIntegerField()),
                ('acct_type', models.CharField(max_length=1)),
                ('check_num', models.PositiveIntegerField()),
                ('cc_num', models.PositiveIntegerField()),
                ('cc_exp_month', models.PositiveIntegerField()),
                ('cc_exp_year', models.PositiveIntegerField()),
                ('cc_vercode', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=40)),
                ('address_line1', models.CharField(max_length=120)),
                ('address_line2', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.PositiveIntegerField()),
                ('bedrooms', models.PositiveIntegerField()),
                ('bathrooms', models.PositiveIntegerField()),
                ('oth_unit_income', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.oth_unit_income')),
                ('reg_unit_expenses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.reg_unit_expenses')),
                ('tenants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.tenants')),
                ('unit_expense_pmts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.unit_expense_pmts')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('company', models.CharField(max_length=80)),
                ('address_line1', models.CharField(max_length=120)),
                ('address_line2', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.PositiveIntegerField()),
                ('ovrhd_expense_pmts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.ovrhd_expense_pmts')),
                ('reg_ovrhd_expenses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.reg_ovrhd_expenses')),
                ('units', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.units')),
            ],
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
