from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView,DetailView

from .models import Property

class PropertyList(ListView):
    
    model = Property

    ## filter
    ## paggination


class PropertyDetail(DetailView):
     model = Property

    ##book