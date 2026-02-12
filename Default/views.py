from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def home(request):

    return render(request,'Default/home.html')




#@login_required
def dashboard5(request):

    user = request.user
    role = None

    if user.groups.filter(name="Executive").exists():
        role = "Executive"

    elif user.groups.filter(name="Manager").exists():
        role = "Manager"

    elif user.groups.filter(name="UwsAdmin").exists():
        role = "UwsAdmin"

    elif user.groups.filter(name="ClientAdmin").exists():
        role = "ClientAdmin"

    else:
        role = "Client"

    context = {
        "role": role,
        "user": user,
    }

    return render(request, "Default/dashboard5.html", context)


def index(request):
    return render(request, 'Default/index.html')
def dashboard(request):
    return render(request, 'Default/dashboard.html')

def dasboardbase(request):
    return render(request,'dashboardbase.html')

def base(request):
    return render(request,'base2.html')

