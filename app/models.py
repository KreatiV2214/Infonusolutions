from django.db import models
from datetime import datetime

# Create your models here.
class offerinfo(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    Instock = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    
class productinfo(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    Instock = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    
    
    def __str__(self):
        return self.name