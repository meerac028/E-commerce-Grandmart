from django.db import models

# Create your models here.
class AddcatDb(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Categoryimage = models.ImageField(upload_to="Images", null=True, blank=True)

class AddproDb(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Product_image = models.ImageField(upload_to="Images", null=True, blank=True)