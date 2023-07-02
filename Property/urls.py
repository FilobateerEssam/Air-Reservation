from django.contrib import admin
from django.urls import path
from . views import PropertyList , PropertyDetail


app_name = 'Property'

urlpatterns = [
    path('', PropertyList.as_view(), name='property_list'),
    #take slug type : slug name
    path('<slug:slug>', PropertyDetail.as_view(),name='property_detail'),
]