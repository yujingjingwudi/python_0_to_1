from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    #阅读量
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

class RoleInfo(models.Model):
    Rname = models.CharField(max_length=20)
    Rgender = models.BooleanField(default=True)
    Rcomment = models.CharField(max_length=200)
    Rbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE)