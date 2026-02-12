from django.contrib.auth.models import Group

def create_user_groups():
    groups = [
        "Executive",
        "Manager",
        "UwsAdmin",
        "ClientAdmin",
        "Client"
    ]

    for group in groups:
        Group.objects.get_or_create(name=group)
