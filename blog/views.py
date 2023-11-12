from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# the view should receive a request to return a response
def blog_view_example(request):
    # you can do whatever you want here, but must return something
    # the response can be an error or something
    return HttpResponse('App blog')