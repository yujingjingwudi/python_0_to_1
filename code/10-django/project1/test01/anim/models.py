from django.db import models

# Create your models here.

class ProductionInfo(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=30,default=None)
    def __str__(self):
        return self.name

class WifeInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    gender = models.BooleanField(default=0)
    point = models.IntegerField()
    hProduction = models.ForeignKey('ProductionInfo',on_delete=models.CASCADE)
    def __str__(self):
        return self.name