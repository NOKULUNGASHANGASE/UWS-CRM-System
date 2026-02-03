from django.shortcuts import render


def home(request):

    return render(request,'Default/home.html')

# Create your views here.
