from django.db import models

# Create your models here.

class Product(models.Model):
    ProductID = models.IntegerField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    ProductRegion = models.CharField(max_length=255)
    ProductPrice = models.IntegerField()
    ProductDescription = models.CharField(max_length=255)
    ProductCompany = models.CharField(max_length=255)
    ProductStock = models.CharField(max_length=255)
    ProductDateCreated = models.DateTimeField()
    ProductDateTour = models.DateTimeField()
# Product.objects.raw('Select * From Product')