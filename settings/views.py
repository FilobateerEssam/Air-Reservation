from django.shortcuts import render

# Create your views here.

def home(request):
    
    template_name = 'settings/home.html'
    return render(request,'settings/home.html',{})