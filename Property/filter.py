import django_filters

# import Model that You will make to him filter 

from .models import Property

class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property 
        fields = ['name', 'description','place', 'category']