from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Product(models.Model):
    shippingChoice=(
        ("FREE SHIPPING","FREE SHIPPING"),
        ("STANDARD SHIPPING","STANDARD SHIPPING"),
    )
    product_id=models.IntegerField()
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300)
    image = models.URLField(null=True, blank=True)
    brand = models.CharField(max_length=200)
    # shipping=models.CharField(max_length=25, choices=shippingChoice, default="FREE SHIPPING")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # category_id = models.IntegerField()
    # featured = models.BooleanField(default=False)
    # active = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)
    # modified = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    rate = models.IntegerField()
    count = models.IntegerField()
    
class Order(models.Model):
    statusChoice = (
        ("PENDING", "Order is pending"),
        ("DISPATCH", "DISPATCH"),
        ("DELIVERED", "DELIVERED"),
    )
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=25, choices=statusChoice, default="PENDING")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    
class Cart(models.Model):
    cart_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    # subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=1)

class User(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    last_name = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    username = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200, validators=[MinLengthValidator(6)]) 

class Invoices(models.Model):
    invoice_id = models.IntegerField()
    client_name = models.CharField(max_length=200)
    date = models.DateField()

class Item(models.Model):
    item_id = models.IntegerField()
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE, related_name="items")
    desc = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)