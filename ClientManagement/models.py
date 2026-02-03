from django.db import models
from django.contrib.auth.models import User
from UwsStaffManagement.models import Division


class ClientAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ClientAdminId=models.AutoField(primary_key=True)
    
    

    def __str__(self):
        return f"{self.user.username} - {self.client.name}"


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ClientId=models.AutoField(primary_key=True)
    ClientAdminId = models.ForeignKey(ClientAdmin, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class ClientDivision(models.Model):
    ClientDivisionId=models.AutoField(primary_key=True)
    ClientId = models.ForeignKey(Client, on_delete=models.CASCADE)
    DivisionId = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.client.name} - {self.name}"



