from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from django.utils import timezone

LISTING_CATEGORY = (
    ("House for Sale", "House for Sale"),
    ("Land for Sale", "Land for Sale"),
    ("Apartment for Rent", "Apartment for Rent"),
)

RENT_PERIOD = (
    ("Short Term(1-6 months)", "Short Term(1-6 months)"),
    ("Long Term(6 months to 1 year)", "Short Term(6 months to 1 year)"),
)


class Listings(models.Model):
    listing_type = models.CharField(max_length=100, choices=LISTING_CATEGORY, default="House for Sale")
    rent_period = models.CharField(max_length=200, choices=RENT_PERIOD, blank=True,
                                   help_text="Only use this field when listing type is apartment for rent")
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
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name
    
    def get_absolute_contact(self):
        return reverse("contact_detail",args={self.id})


class ContactSelf9(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_self9_contact(self):
        return reverse("self9_detail",args={self.id})


class LeaseRegistration(models.Model):
    location_of_land = models.CharField(max_length=250,unique=True)
    size_of_land = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="leases", blank=True)
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    def get_absolute_lease(self):
        return reverse("lease_detail",args={self.id})
