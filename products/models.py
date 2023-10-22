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
    description = models.CharField(default="Complete the Description ASAP", max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # categories = models.ManyToManyField(Category)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    collection = models.ForeignKey('Collection', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    engrave_text = models.CharField(max_length=12, null=True, blank=True)
    engrave_style = models.CharField(max_length=12, null=True, blank=True)
    engrave_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    # Want to remove image_url as think not necessary if AWS enabled
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(default='default_product_image.jpg')

    SIZE_CHOICES = []
    RING_SIZES = [
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        # Add more once get this working
    ]

    CHAIN_LENGTH = [
        ('Small', 'Small 16 inch'),
        ('Medium', 'Medium 18 inch'),
        ('Large', 'Large 20 inch'),
    ]

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        blank=True,
        null=True,
    )


# Want to  Dynamically set size choices based on category
# but could not get working
# have to park size for moment in order to make progress
    # def __init__(self, *args, **kwargs):
    #     super(Product, self).__init__(*args, **kwargs)

    #     # Dynamically set size choices based on category
    #     category = Category.objects.get(name="self.category")
    #     if category.sizeable:
    #         if category.name == 'Rings':
    #             self.SIZE_CHOICES = self.RING_SIZES
    #         elif category.name == 'Pendants':
    #             self.SIZE_CHOICES = self.CHAIN_LENGTH
    #         else:
    #             #  Defensive warning needed, Should not get to this else section
    #             self.SIZE_CHOICES = []
    #     else:
    #         self.SIZE_CHOICES = []


    def __str__(self):
        return self.name
