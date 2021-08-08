from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Listings, ListApartment, NotifyMe
from django.contrib.auth.models import User


@receiver(post_save, Listings)
def new_listing(sender, created, instance, **kwargs):
    if created:
        title = "New Home Listed"
        message = f"{instance.user} added a new home"
        users = User.objects.exclude(id=instance.user.id)

        for user in users:
            NotifyMe.objects.create(user=user, notify_title=title, notify_alert=message, listing_slug=instance.slug)


@receiver(post_save, Listings)
def new_apartment(sender, created, instance, **kwargs):
    if created:
        title = "New Apartment Listed"
        message = f"{instance.user} added a new apartment"
        users = User.objects.exclude(id=instance.user.id)

        for user in users:
            NotifyMe.objects.create(user=user, notify_title=title, notify_alert=message, apartment_slug=instance.slug)