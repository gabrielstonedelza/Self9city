# Generated by Django 3.2.4 on 2021-08-18 11:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0005_alter_listings_rent_period'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaseRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_of_land', models.CharField(max_length=250)),
                ('size_of_land', models.CharField(max_length=250)),
                ('photo', models.ImageField(blank=True, upload_to='leases')),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=500)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='listings',
            name='listing_type',
            field=models.CharField(choices=[('House for Sale', 'House for Sale'), ('Land for Sale', 'Land for Sale'), ('Apartment for Rent', 'Apartment for Rent')], default='House for Sale', max_length=100),
        ),
    ]
