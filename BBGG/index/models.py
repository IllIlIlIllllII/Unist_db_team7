from django.db import models

# Create your models here.
class Userx(models.Model):
    UserID = models.CharField(max_length=100,primary_key=True)
    UserName = models.CharField(max_length=100)
    Passward = models.CharField(max_length=130)
    Gender = models.CharField(max_length=50)
    Age = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20)
    Grade = models.CharField(max_length=20)
    Enrolldate = models.DateTimeField()
    class Meta:
        db_table = 'Userx'