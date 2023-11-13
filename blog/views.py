from django.shortcuts import render

# Create your views here.
# the view should receive a request to return a response
def blog_view_example(request):
    # you can do whatever you want here, but must return something
    # the response can be an error or something
    return render(request, 'blog/index.html', context='We are in the blog page')
    # using the context to send data to the django html file, creating dynamic pages, without using
    # hard coding

def example_view(request):
    return render(request, 'blog/example.html', context='Example page')