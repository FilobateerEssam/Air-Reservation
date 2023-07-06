from __future__ import unicode_literals
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Post,Category
from taggit.models import Tag
from django.db.models import Count
from django.db.models.query_utils import Q


class PostList(ListView):
    model = Post

    paginate_by = 2
    
    def get_queryset(self):
     
     # search by input text which name is q if doesn't exist make it empty
     name = self.request.GET.get('q','')
     object_list = Post.objects.filter(
         
        #Q used to Search in QuerySet 
        #  att from models__name to return name which will used in name search by title or description

         Q(title__icontains=name) | 
         Q(description__icontains=name) 

     )
     return object_list



class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count = Count('post_category'))
        context["tags"] = Tag.objects.all()
        context["recent_posts"] = Post.objects.all()[:3]  # to Return just 3
        return context




class PostBYCategory(ListView):
    model = Post

    def get_queryset(self):
     
     slug = self.kwargs['slug']  # we get the slug from url
     object_list = Post.objects.filter(
         
        #Q used to Search in QuerySet 
        #  att from models__name to return name which will used in slug

         Q(category__name__icontains=slug)
     )
     return object_list

 

class PostBYTags(ListView):
    model = Post


    
    def get_queryset(self):
        
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(tags__name__icontains=slug)
        )
        return object_list
    
