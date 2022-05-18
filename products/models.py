from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.title




from products.models import Product
queryset = Product.objects.all()



# Create your models here.
