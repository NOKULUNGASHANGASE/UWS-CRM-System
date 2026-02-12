from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):

    return render(request,'Default/home.html')



#@login_required
def dashboard(request):

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

    return render(request, "Default/dashboard.html", context)

