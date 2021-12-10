from django.db import models
# Create your models here.

class Purchase(models.Model):
    PurchaseID = models.IntegerField(primary_key=True)
    ProductID = models.ForeignKey("ProductList.Product",related_name="Purchase_product",on_delete = models.DO_NOTHING,db_column="ProductID")
    USERID = models.IntegerField()
    Amount = models.IntegerField()
    PurchaseDate = models.DateTimeField()
    TotalPrice = models.IntegerField()
    Requirement = models.CharField(max_length=255)
    CouponID = models.IntegerField()
    class Meta:
        db_table = 'Purchase'
 