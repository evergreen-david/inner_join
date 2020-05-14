from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    # manufacturer = models.CharField(max_length=30)
    manufacturer = models.ForeignKey('Manufacturer', on_delete = models.SET_NULL, null=True)
    price = models.IntegerField()
    product_type = models.CharField(max_length=30)

    class Meta:
        db_table = 'product'

class Stock(models.Model):
    product = models.ForeignKey('Product', on_delete = models.SET_NULL, null=True)
    received_data = models.DateTimeField(blank=True, auto_now_add=True)
    volume = models.IntegerField()

    class Meta:
        db_table = 'stock'

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'manufacturer'

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table ='user'

class UserProfile(models.Model):
    user = models.ForeignKey('User', on_delete = models.SET_NULL, null=True)
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)

    class Meta:
        db_table = 'user_profile'

