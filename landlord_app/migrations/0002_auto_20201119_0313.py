# Generated by Django 3.1.1 on 2020-11-19 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landlord_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address_line1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address_line2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user',
            name='zipcode',
        ),
    ]