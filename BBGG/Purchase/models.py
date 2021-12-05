from django.db import models
# Create your models here.

class Purchase(models.Model):
    PurchaseID = models.IntegerField(primary_key=True)
    ProductID = models.IntegerField()
    USERID = models.IntegerField()
    Amount = models.IntegerField()
    PurchaseDate = models.DateTimeField()
    TotalPrice = models.IntegerField()
    Requirement = models.CharField(max_length=255)
    CouponID = models.IntegerField()
    class Meta:
        db_table = 'Purchase'
 