# Generated by Django 4.1.7 on 2023-04-03 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truckr', '0006_shipmentout'),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('employeeID', models.IntegerField(primary_key=True, serialize=False)),
                ('accountType', models.CharField(max_length=5)),
            ],
        ),
    ]
