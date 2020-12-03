# Generated by Django 3.1.1 on 2020-12-03 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord_app', '0012_auto_20201202_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='mtom',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='mtomnotice',
            field=models.CharField(default='Letter', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='mtomnoticedays',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
    ]