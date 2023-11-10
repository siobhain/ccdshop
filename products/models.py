from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=25, null=True, blank=True)
    engravable = models.BooleanField(default=False)
    sizeable = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Collection(models.Model):
    name = models.CharField(max_length=20)
    friendly_name = models.CharField(max_length=25, null=True, blank=True)
    description = models.CharField(
        default="Complete the Description ASAP", max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default='default_product_image.jpg')
    sizeable = models.BooleanField(default=False, null=True, blank=True)
    engrave = models.BooleanField(default=False)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    collection = models.ForeignKey(
        'Collection', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    rating = models.DecimalField(
        decimal_places=1, max_digits=2, null=True, blank=True)

    def __str__(self):
        return self.name

