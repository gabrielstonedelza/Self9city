# Generated by Django 3.2.4 on 2021-08-06 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_listings_listing_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSelf9',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='listings',
            name='full_location',
            field=models.CharField(max_length=500),
        ),
    ]