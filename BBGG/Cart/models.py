from django.db import models

# Create your models here.
class Cart(models.Model):
    ProductID = models.IntegerField(primary_key=True)
    UserID = models.IntegerField()
    Amount = models.IntegerField()
    ProductName = models.CharField(max_length=255)
    ProductPrice = models.IntegerField()
    class Meta:
        db_table = 'Cart'