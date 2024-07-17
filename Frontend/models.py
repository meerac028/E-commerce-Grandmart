from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class RegistrationDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class CartDb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Productname = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Sing_price = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)

class CheckoutDb(models.Model):
    Firstname = models.CharField(max_length=100,null=True,blank=True)
    Lastname = models.CharField(max_length=100,null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Town = models.CharField(max_length=100,null=True,blank=True)
    Postcode = models.IntegerField(null=True,blank=True)
    Phonenum = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)