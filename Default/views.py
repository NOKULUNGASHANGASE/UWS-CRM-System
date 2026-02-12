from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):

    return render(request,'Default/home.html')

def index(request):
    return render(request, 'Default/index.html')
def dashboard(request):
    return render(request, 'Default/dashboard.html')

def dasboardbase(request):
    return render(request,'dashboardbase.html')

def base(request):
    return render(request,'base2.html')
