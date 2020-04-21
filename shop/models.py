from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, default=1)
    product_name = models.CharField(max_length=300, default='')
    category = models.CharField(max_length=100, default='')
    subcategory = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=700, default='')
    pub_date = models.DateField(default='20/4/2020')
    image = models.CharField(max_length=500, default='')
    objects = models.Manager()


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True, default=1)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    cell = models.IntegerField(default=0)
    desc = models.CharField(max_length=500, default='')
    objects = models.Manager()


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True, default=1)
    items_json = models.CharField(max_length=5000, default='')
    name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=500, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    zip_code = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    objects = models.Manager()
