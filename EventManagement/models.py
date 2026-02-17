from django.db import models
#from django.contrib.auth.models import User
from ClientManagement.models import Organisation
from UwsStaffManagement.models import UwsAdmin, Division, Manager

class Event(models.Model):
    EventId= models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    UwsAdminId= models.ForeignKey(UwsAdmin, on_delete=models.SET_NULL, null=True)
    ManagerId= models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    #created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Attendee(models.Model):
    AttendeeId= models.AutoField(primary_key=True)
    ClientId = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    EventId = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Newsletter(models.Model):
    NewsletterId= models.AutoField(primary_key=True)
    EventId = models.ForeignKey(Event, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

