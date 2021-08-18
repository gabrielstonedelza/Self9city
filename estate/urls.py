from django.urls import path, include
from . import views

urlpatterns = [
    # listings
    path("", views.index, name="index", ),
    path("admin_listings/", views.my_index, name="my_index", ),
    path('listing/new/', views.create_listing, name='create_listing'),
    path('listing/add_to_gallery/', views.add_to_listing_gallery, name='add_to_gallery'),
    path('about/', views.about_us, name='about'),
    path("listing_detail/<str:slug>/", views.listing_detail, name="listing_detail"),
    path("admin_listing_detail/<str:slug>/", views.admin_listing_detail, name="admin_listing_detail"),
    path('search/', views.search, name="search"),
    path('contact-lists/', views.contacted_lists, name="contact-lists"),
    path('buy/', views.buy_lists, name="buying"),
    path('rent/', views.rent_lists, name="rents"),
    path('lease/', views.register_lease, name='lease'),
    path('lease/<int:id>/',views.lease_detail,name="lease_detail"),
    path('self9/<int:id>/',views.self9_detail,name="self9_detail"),
    path('contact/<int:id>/',views.contact_detail,name="contact_detail"),

    # api
    # path('all_listings/', views.AllListings.as_view()),
    # path('listing/<str:slug>/', views.listing_detail),
    # path('listings/<str:slug>/', views.listings_detail),
    # path('contact_us/<str:slug>/', views.contactus),
    # path('contact_self9/', views.contactself9),
    # path('listing_search/<str:name>/', views.listing_filter)
    # path('search/', views.search_queries, name='search'),
    # path('about/', views.about_us, name="about"),
]
