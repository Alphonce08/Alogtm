from django.db import models

# Create your models here.
class car(models.Model):
    car_brand = models.CharField(max_lenght=100)
    car_ksh = models.CharField(max_lenght=5)
    car_origin = models.CharField(max_lenght=10)
    car_color = models.CharField(max_lenght=100)
    
  
    def __str__(self):
        return self.car_brand
        