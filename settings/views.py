from django.shortcuts import render

from Property.models import Property , Place , Category  # that have all places stored in DB Property Model
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    
    places = Place.objects.all().annotate(property_count = Count('property_place'))
    category = Category.objects.all() 

    resturant_list =  Property.objects.filter(category__name= 'Restaurant')[:5]
    hotels_list = Property.objects.filter(category__name= 'Hotels')[:4]
    places_list = Property.objects.filter(category__name= 'Places')[:4]

    recent_posts = Post.objects.all()[:4]

    users_count = User.objects.all().count()
    hotels_count = Property.objects.filter(category__name= 'Hotels').count()
    resturant_count = Property.objects.filter(category__name= 'Restaurant').count()
    places_count = Property.objects.filter(category__name= 'Places').count()

    template_name = 'settings/home.html'
    return render(request,'settings/home.html',{
        'places' : places ,
        'category': category,
        'resturant_list': resturant_list,
        'hotels_list': hotels_list,
        'places_list': places_list,
        'recent_posts':recent_posts,
        'users_count':users_count,
        'hotels_count':hotels_count,
        'resturant_count':resturant_count,
        'places_count':places_count,

    })


def home_search(request):

    name = request.GET.get('name')       # which put in frontend to use in backend
    place  = request.GET.get('place')    # which put in frontend to use in backend

    property_list = Property. objects.filter(
        Q(name__icontains = name) &   # & and if you want to use | or  # name inside Property Model att
        Q(place__name__icontains= place)          # place --> name inside Property Model att  
    ) 

    return render(request, 'settings/home_search.html',{'property_list':property_list})


def category_filter(request,category):
    
    category = Category.objects.get(name =category )

    # ***********  Filter ALL Properties on List ***********

    property_list = Property. objects.filter(category = category ) 

    return render(request, 'settings/home_search.html',{'property_list':property_list})

def contact_us(request):
    pass