# Generated by Django 3.2.4 on 2021-08-18 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0006_auto_20210818_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaseregistration',
            name='location_of_land',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
