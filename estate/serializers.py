from rest_framework import serializers
from .models import Listings, ListingGallery, ContactUs, ContactSelf9


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listings
        fields = ['id', 'listing_type', 'full_location', 'rooms', 'baths', 'size_of_building', 'photo', 'price',
                  'description',
                  'date_posted', 'slug', 'get_absolute_url', 'get_listing_image', 'views', 'can_pay_monthly']


class ListingGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingGallery
        fields = ['id', 'listing', 'images', 'date_posted', 'get_listings_image']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'listing', 'full_name', 'email', 'phone', 'message']
        read_only_fields = ['listing']


class ContactSelf9Serializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSelf9
        fields = ['id', 'name', 'email', 'phone', 'message']
