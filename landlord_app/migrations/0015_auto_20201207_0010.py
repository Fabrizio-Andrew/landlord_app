# Generated by Django 3.1.1 on 2020-12-07 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord_app', '0014_auto_20201204_0333'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Evict_Notice',
        ),
        migrations.DeleteModel(
            name='Tenant_Payment',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='tenant_end',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='tenant_start',
        ),
        migrations.AlterField(
            model_name='lease',
            name='rollover',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
