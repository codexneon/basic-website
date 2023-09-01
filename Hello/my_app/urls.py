from django.contrib import admin
from django.urls import path
from my_app import views

admin.site.site_header = "MakemyTrip Admin"
admin.site.site_title = "MakemyTrip Admin Portal"
admin.site.index_title = "Welcome to MakemyTrip Portal"

urlpatterns = [
    path("", views.index, name='my_app'),
    path("about", views.about, name= 'about'),
    path("services", views.services, name= 'services'),
    path("contact", views.contact, name= 'contact'),
]
