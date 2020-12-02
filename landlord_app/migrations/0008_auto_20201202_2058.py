# Generated by Django 3.1.1 on 2020-12-02 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landlord_app', '0007_auto_20201120_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('abbrev', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('failtopay', models.BooleanField()),
                ('failtopaydays', models.IntegerField()),
                ('failtopaynotice', models.CharField(max_length=20)),
                ('failtopaynoticedays', models.IntegerField()),
                ('posethreat', models.BooleanField()),
                ('posethreatnotice', models.CharField(max_length=20)),
                ('posethreatnoticedays', models.IntegerField()),
                ('violatelease', models.BooleanField()),
                ('violateleasenotice', models.CharField(max_length=20)),
                ('violateleasenoticedays', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='unit',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord_app.state'),
        ),
    ]
