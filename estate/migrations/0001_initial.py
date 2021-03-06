# Generated by Django 3.2.4 on 2021-07-30 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_location', models.CharField(max_length=200)),
                ('rooms', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('size_of_building', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='listings')),
                ('price', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, default='', max_length=100)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('can_pay_monthly', models.CharField(max_length=200)),
                ('approved', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListingGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='listing_gallery')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.listings')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=500)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estate.listings')),
            ],
        ),
    ]
