from django.db import models

# Create your models here.
class Cart(models.Model):
    CartID = models.IntegerField(primary_key=True)
    ProductID = models.ForeignKey("ProductList.Product",related_name="Cart_product",on_delete = models.DO_NOTHING,db_column="ProductID")
    UserID = models.IntegerField()
    Amount = models.IntegerField()
    ProductName = models.CharField(max_length=255)
    ProductPrice = models.IntegerField()
    class Meta:
        db_table = 'Cart'
        unique_together = (('ProductID','UserID'),)