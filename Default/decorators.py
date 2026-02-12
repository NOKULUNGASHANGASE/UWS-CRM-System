from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group


#this code licks the view only the assigned role will have access(@role_required("Executive"))
#def role_required(role):
    #def check(user):

        #group = Group.objects.all()
        #users = group.user_set.all()
        #print("groups : ", group)
        #return user.is_authenticated and user.groups.filter(name=role).exists()
    #return user_passes_test(check)


def role_required(role):
    def check(user):
        
        return user.is_authenticated and user.groups.filter(name=role).exists()
    return user_passes_test(check)

