
from django.shortcuts import get_object_or_404, redirect, render
from .models import Executive, Division, Manager
from Default.decorators import role_required
from .models import Division,Executive
from django.contrib.auth.models import User
from Default.utils import assign_user_to_group
from django.contrib import messages
from django.contrib.auth.hashers import make_password
import string
import secrets
from django.core.mail import send_mail
from django.conf import settings
from .sendemail import send_manager_assignment_email, send_password_update_email




def create_executive(request):

    if request.method == "POST":
        Executive.objects.create(
            user=request.user,

            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
        )
        return redirect("executive_list")

    return render(request, 'UwsStaffManagement/create_executive.html')

def update_executive(request, pk):

    executive = get_object_or_404(Executive, pk=pk)

    if request.method == "POST":

        executive.name = request.POST.get("name")
        executive.email = request.POST.get("email")
        executive.phone = request.POST.get("phone")
        executive.address = request.POST.get("address")

        executive.save()

        return redirect("executive_list")

    return render(request, "UwsStaffManagement/update_executive.html", { "executive": executive })



def executive_list(request):

    executives = Executive.objects.all()

    return render(request, 'UwsStaffManagement/executive_list.html', {"executives": executives})

def delete_executive(request, pk):

    executive = get_object_or_404(Executive, pk=pk)

    executive.delete()

    return redirect("executive_list")




    
@role_required("Executive")
def create_division(request):

    executive = get_object_or_404(Executive, user=request.user)

    if request.method == 'POST':
        Division.objects.create( name=request.POST["name"], ExecutiveId=executive, )
        return redirect("dashboard")  

    return render(request, 'UwsStaffManagement/create_division.html')
    

def division_list(request):

    divisions = Division.objects.all()

    return render(request, 'UwsStaffManagement/division_list.html', {"divisions": divisions})


@role_required("Executive")
def update_division(request, pk):

    executive = get_object_or_404(Executive, user=request.user)

    division = get_object_or_404( Division, pk=pk, ExecutiveId=executive )

    if request.method == "POST":

        division.name = request.POST.get("name")
        division.save()

        return redirect("division_list")

    return render(request, "UwsStaffManagement/update_division.html", { "division": division })


@role_required("Executive")
def delete_division(request, pk):

    executive = get_object_or_404(Executive, user=request.user)

    division = get_object_or_404( Division, pk=pk, ExecutiveId=executive )

    division.delete()

    return redirect("division_list")

    
@role_required("Executive")
def assign_manager(request):
    executive = get_object_or_404(Executive, user=request.user)
    divisions = Division.objects.filter(ExecutiveId=executive)

    if request.method == "POST":
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        division_id = request.POST.get("division")
        title = request.POST.get("title")
        phone = request.POST.get("phone")

        # letCheck if user exists
        if User.objects.filter(username=email).exists():
           messages.error = (request,"A user with this email already exists")
           return render(request, "UwsStaffManagement/assign_manager.html", {"divisions": divisions})
        else:

            generated_password = generate_password()
            # let Create user here taking from the django user
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=generated_password 
                
            )

        division = get_object_or_404(Division, pk=division_id)
        assign_user_to_group(user, "Manager")

        Manager.objects.create(
            user=user,
            DivisionId=division,
            Tittle=title,
            phone=phone
        )
        send_manager_assignment_email(
                first_name=first_name,
                last_name=last_name,
                email=email,
                division_name=division.name,
                generated_password=generated_password,
            )

        return redirect("manager_list")

    return render(request, "UwsStaffManagement/assign_manager.html", {"divisions": divisions})




@role_required("Executive")
def manager_list(request):

    executive = get_object_or_404(Executive, user=request.user)
    
    managers = Manager.objects.select_related('DivisionId', 'user').all()
   
    #managers = Manager.objects.all()

    print("ALL managers:", managers.count())

   
    
    return render(request, "UwsStaffManagement/manager_list.html", {"managers": managers})



@role_required("Executive")
def update_manager(request, pk):
    executive = get_object_or_404(Executive, user=request.user)
    manager = get_object_or_404( Manager, pk=pk, DivisionId__ExecutiveId=executive)
    divisions = Division.objects.filter(ExecutiveId=executive)

    if request.method == "POST":

        
        user = manager.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")

        new_password = request.POST.get("password")

        
        
        if new_password:
            user.set_password(new_password)
            send_password_update_email(user, new_password)
                    

            user.save()

       
        division_id = request.POST.get("division")
        manager.DivisionId = get_object_or_404( Division, pk=division_id, ExecutiveId=executive)

        manager.Tittle = request.POST.get("title")
        manager.phone = request.POST.get("phone")

        manager.save()

        return redirect("manager_list")

    return render( request, "UwsStaffManagement/update_manager.html",  { "manager": manager, "divisions": divisions, }, )




def generate_password(length=10):

    characters = string.ascii_letters + string.digits + string.punctuation
    
    return ''.join(secrets.choice(characters) for _ in range(length))

