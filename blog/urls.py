from django.urls import path
from . import views

    
# blog/
urlpatterns = [
    path('', views.blog_view_example),
    path('example/', views.example_view),
]