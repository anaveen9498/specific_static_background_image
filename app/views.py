from django.shortcuts import render

# Create your views here.


def static_specific_webpage(request):
    return render(request,'static_specific_webpage.html')
