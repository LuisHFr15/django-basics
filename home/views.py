from django.shortcuts import render

# Create your views here.
def home(request):
    print('home')
    return render(request, 'home/index.html', context={'text': 'We are in the Home page',
                                                       'title':'Home Page'})