from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse

LISTING_CATEGORY = (
    ("House for Sale", "House for Sale"),
    ("Land for Sale", "Land for Sale"),
    ("Apartment for rent", "Apartment for rent"),
)


class Listings(models.Model):
    listing_type = models.CharField(max_length=100, choices=LISTING_CATEGORY, default="House for Sale")
    full_location = models.CharField(max_length=500)
    rooms = models.IntegerField()
    baths = models.IntegerField()
    size_of_building = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="listings")
    price = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=100, default='', blank=True)
    views = models.IntegerField(default=0, blank=True)
    can_pay_monthly = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_location

    def get_absolute_listing(self):
        return reverse("listing_detail", args={self.slug})

    def get_absolute_url(self):
        return reverse("admin_listing_detail", args={self.slug})

    def get_listing_image(self):
        if self.photo:
            return "http://64.227.22.163/" + self.photo.url
        return ''

    def save(self, *args, **kwargs):
        value = self.full_location
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class ListingGallery(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="listing_gallery")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.listing.full_location

    def get_listings_image(self):
        if self.images:
            return "http://64.227.22.163/" + self.images.url
        return ''


class ContactUs(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.full_name


class ContactSelf9(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
