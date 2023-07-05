from django.shortcuts import render , redirect
from django.views.generic.edit import FormMixin

# Create your views here.

from django.views.generic import ListView,DetailView

from .models import Property
from .forms import PropertyBookForm
from .filter import PropertyFilter
from django_filters.views import FilterView  # from Doc read

class PropertyList(FilterView):
    
    model = Property
    
    ## paggination

    paginate_by = 1     # Max Num of Cards inside the page 

    ## filter

    filterset_class = PropertyFilter
    template_name = 'Property/property_list.html'

class PropertyDetail(FormMixin , DetailView):
     
     
     model = Property

     form_class = PropertyBookForm


    ##book
    ## Related by filter in the same Category 

     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         #["any name"]      =  class have att that i will filter by 
         # (name of att = to get in the same category will use self.get_object().att ) [from 0 : to 2]
         context["related"] = Property.objects.filter(category = self.get_object().category)[:2]
         return context
     

     def post(self,request,*args,**kwargs):

         form = self.get_form()

         if form.is_valid():
             myform = form.save(commit = False)
             myform.property = self.get_object()
             myform.user = request.user
             myform.save()


             return redirect('/')





    

    