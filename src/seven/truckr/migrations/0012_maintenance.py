# Generated by Django 4.1.7 on 2023-04-13 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truckr', '0011_partslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='maintenance',
            fields=[
                ('maintID', models.IntegerField(primary_key=True, serialize=False)),
                ('vehID', models.IntegerField()),
                ('description', models.CharField(max_length=30)),
                ('completed', models.DateTimeField()),
                ('partsList', models.IntegerField()),
            ],
        ),
    ]
