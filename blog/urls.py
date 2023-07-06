from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
   
    path('',views.PostList.as_view() , name='post_list'),
    path('<slug:slug>', views.PostDetail.as_view() , name='post_detail'),
    
    path('category/<str:slug>', views.PostBYCategory.as_view() , name='post_by_category'),
    path('tags/<str:slug>', views.PostBYTags.as_view() , name='post_by_tags'),
    
]