from django.urls import path
from . import views


# name espace -> important to avoid name conflicts
app_name = 'blog'
    
# blog/
urlpatterns = [
    path('', views.blog_view_example, name='home'),
    path('example/', views.example_view, name='example'),
]
# setting the name is important to dynamic urls while creating the site