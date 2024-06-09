from django.db import models

# Create your models here.
class Car(models.Model):    
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    brand = models.ForeignKey('brands.CarBrand', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Comments(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
