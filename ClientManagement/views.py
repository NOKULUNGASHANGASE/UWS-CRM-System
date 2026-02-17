from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Organisation, OrganisationAdmin

# Create your views here.

def organisation_admin_list(request):
    admins = OrganisationAdmin.objects.all()
    return render(request, "ClientManagement/organisation_admin_list.html", {
        "admins": admins
    })

def create_organisation_admin(request):
    if request.method == 'GET':
        
        
        return render(request, 'ClientManagement/create_organisation_admin.html')
    
    
    if request.method == "POST":
        user_id = request.POST["user"]
        user = get_object_or_404(User, id=user_id)

        OrganisationAdmin.objects.create(user=user)

        return redirect("organisation_admin_list")

    users = User.objects.all()
    return render(request, "ClientManagement/create_organisation_admin.html", {
        "users": users
    })

def delete_organisation_admin(request, pk):
    admin = get_object_or_404(OrganisationAdmin, pk=pk)
    
    if request.method == "POST":
       admin.delete()
       return redirect("organisation_admin_list")

    return render(request, "ClientManagement/delete_organisation_admin.html", {
        "admin": admin
    })


def organisation_list(request):
    organisations = Organisation.filter(status = 'Active')
    return render(request, "ClientManagement/organisation_list.html", {
        "organisations": organisations
    })

def create_organisation(request):
    if request.method == "POST":
        Organisation.objects.create(
            user=request.user,
            organisation_admin_id=request.POST["admin"],
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            address=request.POST["address"],
        )
        return redirect("organisation_list")

    admins = OrganisationAdmin.objects.all()
    return render(request, "ClientManagement/create_organisation.html", {
        "admins": admins
    })

def update_organisation(request, pk):
    organisation = get_object_or_404(Organisation, pk=pk)

    if request.method == "POST":
        organisation.name = request.POST["name"]
        organisation.email = request.POST["email"]
        organisation.phone = request.POST["phone"]
        organisation.address = request.POST["address"]
        organisation.organisation_admin_id = request.POST["admin"]

        organisation.save()
        return redirect("organisation_list")
    else:
        admins = OrganisationAdmin.objects.filter(status = 'Active')
        return render(request, "ClientManagement/update_organisation.html", {
            "organisation": organisation,
            "admins": admins
        })

def delete_organisation(request, pk):
    organisation = get_object_or_404(Organisation, pk=pk)
    
    if request.method == "POST":
       organisation.status = "Deleted"
       organisation.save()
       return redirect("organisation_list")

    return render(request, "ClientManagement/delete_organisation.html", {
        "organisation": organisation
    })
