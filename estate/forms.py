from django import forms
from .models import Listings, ListingGallery, ContactUs


class NewListingForm(forms.ModelForm):
    class Meta:
        model = Listings
        fields = ['full_location', 'rooms', 'baths', 'size_of_building', 'photo', 'price', 'description',
                  'can_pay_monthly']


class AddToListingGallery(forms.ModelForm):
    images = forms.ImageField(label="Select Images", widget=forms.FileInput(
        attrs={"class": "form-control", "multiple": "multiple", "name": "images"}))

    class Meta:
        model = ListingGallery
        fields = ['listing', 'images']


class ContactForm(forms.ModelForm):
    message = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'your message', "id": "cform"}))

    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'phone', 'message']
