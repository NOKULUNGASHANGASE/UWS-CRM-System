from django.db import models
from django.contrib.auth.models import User


class Executive(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ExecutiveId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Executive - {self.user.username}"

class Division(models.Model):
    DivisionId=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ExecutiveId = models.ForeignKey(Executive, on_delete=models.DO_NOTHING, null=True,blank=True)
    def __str__(self):
        return self.name

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ManagerId= models.AutoField(primary_key=True)
    DivisionId= models.ForeignKey(Division, on_delete=models.DO_NOTHING, null=True,blank=True)
    Tittle = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Manager - {self.user.username}"


class UwsAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    UwsAdminId= models.AutoField(primary_key=True)
    DivisionId= models.ForeignKey(Division, on_delete=models.DO_NOTHING, null=True,blank=True)
    Tittle = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Admin - {self.user.username}"

