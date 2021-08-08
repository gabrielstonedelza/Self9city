from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .process_mail import send_my_mail
from .models import Listings, ListingGallery, ContactUs, ContactSelf9

from .forms import (NewListingForm, AddToListingGallery, ContactForm)
from django.conf import settings
from .serializers import ListingSerializer, ListingGallerySerializer, ContactSerializer, ContactSelf9Serializer

# api stuff
from rest_framework import viewsets, generics, permissions, status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import filters


class AllListings(generics.ListAPIView):
    queryset = Listings.objects.all().order_by('-date_posted')
    serializer_class = ListingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['full_location']


@api_view(['GET'])
def listing_filter(request, name):
    listing = Listings.objects.filter(full_location__icontains=name)
    serializer = ListingSerializer(listing, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listings_detail(request, slug):
    listing = get_object_or_404(Listings, slug=slug)
    serializer = ListingSerializer(listing, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def listing_detail(request, slug):
    listing = get_object_or_404(Listings, slug=slug)
    listing_gallery = ListingGallery.objects.filter(listing=listing)
    if listing:
        listing.views += 1
        listing.save()
    serializer = ListingGallerySerializer(listing_gallery, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def contactus(request, slug):
    listing = get_object_or_404(Listings, slug=slug)
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(listing=listing)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def contactself9(request):
    serializer = ContactSelf9Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def csrf_failure(request, reason=""):
    return render(request, "estate/403_csrf.html")


def search_queries(request):
    global search_listings
    query = request.GET.get('q', None)
    if query is not None:
        search_listings = Listings.objects.filter(
            Q(full_location__icontains=query)
        )

    context = {
        'all_listings': search_listings,
    }

    if request.is_ajax():
        search_results = render_to_string("estate/search.html", context, request=request)
        return JsonResponse({
            'form': search_results
        })


@login_required()
def my_index(request):
    search_listings = request.GET.get('q', '')
    if search_listings:
        all_listings = Listings.objects.filter(
            Q(full_location__icontains=search_listings)
        )
    else:
        all_listings = Listings.objects.all().order_by('-date_posted')

    paginator = Paginator(all_listings, 50)
    page = request.GET.get('page')
    all_listings = paginator.get_page(page)

    context = {
        "all_listings": all_listings,
    }

    return render(request, "estate/my_index.html", context)


def index(request):
    search_listings = request.GET.get('q', '')
    if search_listings:
        all_listings = Listings.objects.filter(
            Q(full_location__icontains=search_listings)
        )
    else:
        all_listings = Listings.objects.all().order_by('-date_posted')

    paginator = Paginator(all_listings, 50)
    page = request.GET.get('page')
    all_listings = paginator.get_page(page)

    context = {
        "all_listings": all_listings,
    }
    return render(request, "estate/index.html", context)


def admin_listing_detail(request, slug):
    listing = get_object_or_404(Listings, slug=slug)
    listing_gallery = ListingGallery.objects.filter(listing=listing)

    if listing:
        listing.views += 1
        listing.save()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')

            ContactUs.objects.create(full_name=fname, email=email, phone=phone, message=message)
            messages.success(request, f"Thank you,we will get back to you soon.")
            send_my_mail(f"Hi from Safe9 City", settings.EMAIL_HOST_USER, email, {"name": fname},
                         "email_templates/success.html")
            send_my_mail(f"New Message", settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER,
                         {"name": fname, "email": email, "message": message},
                         "email_templates/contact_success.html")
            return redirect('listing_detail', listing.slug)
    else:
        form = ContactForm()

    context = {
        "listing": listing,
        "form": form,
        "listing_gallery": listing_gallery,
    }

    return render(request, "estate/listing_detail.html", context)


@login_required()
def add_to_listing_gallery(request):
    if request.method == "POST":
        form = AddToListingGallery(request.POST, request.FILES)
        if form.is_valid():
            listing = form.cleaned_data.get('listing')
            images = request.FILES.getlist('images')

            for image in images:
                ListingGallery.objects.create(listing=listing, images=image)
            messages.success(request, f'images were added to {listing}"s gallery')
            return redirect('my_index')
        else:
            messages.info(request, 'something went wrong')
    else:
        form = AddToListingGallery()

    context = {
        "form": form
    }

    return render(request, "estate/add_gallery.html", context)


@login_required()
def create_listing(request):
    if request.method == "POST":
        form = NewListingForm(request.POST, request.FILES)
        if form.is_valid():
            full_location = form.cleaned_data.get('full_location')
            rooms = form.cleaned_data.get('rooms')
            baths = form.cleaned_data.get('baths')
            size_of_building = form.cleaned_data.get('size_of_building')
            photo = form.cleaned_data.get('photo')
            price = form.cleaned_data.get('price')
            description = form.cleaned_data.get('description')
            can_pay_monthly = form.cleaned_data.get('can_pay_monthly')
            Listings.objects.create(full_location=full_location, rooms=rooms, baths=baths,
                                    size_of_building=size_of_building,
                                    photo=photo, price=price, description=description, can_pay_monthly=can_pay_monthly)
            messages.success(request, 'listing added but still awaiting approval')
            return redirect('my_index')
        else:
            messages.info(request, "something went wrong")
    else:
        form = NewListingForm()

    context = {
        "form": form,
    }
    return render(request, "estate/newlisting.html", context)


def about_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')

            ContactUs.objects.create(full_name=fname, email=email, phone=phone, message=message)
            # messages.success(request, f"Thank you,we will get back to you soon.")
            send_my_mail(f"Hi from Safe9 City", settings.EMAIL_HOST_USER, email, {"name": fname},
                         "email_templates/success.html")
            send_my_mail(f"New Message", settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER,
                         {"name": fname, "email": email, "message": message},
                         "email_templates/contact_success.html")
            return redirect('about')
    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    return render(request, "estate/about_us.html", context)
