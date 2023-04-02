# Generated by Django 4.1.7 on 2023-04-02 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truckr', '0005_remove_shipmentin_clientid_shipmentin_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='shipmentOut',
            fields=[
                ('shipID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('vehID', models.IntegerField()),
                ('departure', models.DateTimeField()),
                ('estArrival', models.DateTimeField()),
                ('arrived', models.BooleanField()),
                ('payment', models.BooleanField()),
                ('driver', models.IntegerField()),
                ('manifest', models.IntegerField()),
                ('purchaseOrder', models.IntegerField()),
                ('clientName', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=6)),
            ],
        ),
    ]
