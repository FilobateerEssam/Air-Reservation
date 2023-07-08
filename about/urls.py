from django.urls import path,include
from . views import AboutView

app_name = 'about'
urlpatterns = [
    
    path('',AboutView.as_view(),name='about')
    
]