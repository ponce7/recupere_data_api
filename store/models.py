from django.db import models
class Category (models.Model):
    name = models.CharField(max_length=200)
    

class Product (models.Model):
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/items-grid', null=False, blank=False)
    description= models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default= True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name