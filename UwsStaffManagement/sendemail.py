from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.conf import settings


def send_manager_assignment_email(
    first_name,
    last_name,
    email,
    division_name,
    generated_password,
):

    subject = "Manager Assignment - UWS CRM System"

    message = f"""
Hello {first_name} {last_name},

You have been assigned as a Manager.

Division: {division_name}

Login details:

Username: {email}
Password: {generated_password}

Please log in and change your password.

UWS CRM System
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )


def send_password_update_email(user, new_password):

    subject = "Password Updated - UWS CRM System"

    message = f"""
Hello {user.first_name},

Your password has been updated.

Username: {user.username}
Password: {new_password}

UWS CRM System
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )

