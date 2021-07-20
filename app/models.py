from django.db import models

# Create your models here.
global length
length = 255
class Admin(models.Model):
    email = models.EmailField(max_length=length,unique=True,default="Email")
    password = models.CharField(max_length=length,default="Password")
    role = models.CharField(max_length = length,default="Role")
    fotp = models.IntegerField(default=123456)
    Is_created = models.DateField(auto_now_add=True)
    Is_activated = models.BooleanField(default=False)

class Hr(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=length,default="First Name")
    lastname = models.CharField(max_length=length,default="Last Name")
    address = models.CharField(max_length=length,default = "Address")
    bdate = models.DateField(null=True)
    phone = models.BigIntegerField(default=1234567890)
    gender = models.CharField(max_length=length,default="Gender")
    marital = models.CharField(max_length=length,default="marital status")

class Emp(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=length,default="First Name")
    lastname = models.CharField(max_length=length,default="Last Name")
    address = models.CharField(max_length=length,default = "Address")
    bdate = models.DateField(null=True)
    phone = models.BigIntegerField(default=1234567890)
    gender = models.CharField(max_length=length,default="Gender")
    marital = models.CharField(max_length=length,default="marital status")