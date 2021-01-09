from django.db import models

# Create your models here.

class PicClass(models.Model):
    picture = models.ImageField(verbose_name='图片位置',upload_to='staticsmiddleware')
    def idd(self):
        return self.picture
    def __str__(self):
        return '图片'
    idd.short_description = "图片位置"