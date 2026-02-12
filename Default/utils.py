from django.contrib.auth.models import Group

def assign_user_to_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
    except Group.DoesNotExist:
        print(f"Group '{group_name}' does not exist.")
