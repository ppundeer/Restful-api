from django.db import models

class superstore(models.Model):
    order_id = models.CharField(max_length=20)
    order_date = models.DateTimeField()
    ship_date = models.DateTimeField()
    ship_mode = models.CharField(max_length=20)
    customer_id = models.CharField(max_length=20)
    customer_name = models.TextField(max_length=25)
    segment = models.TextField(max_length=25)
    country = models.TextField(max_length=25)
    city = models.TextField(max_length=25)
    state = models.TextField(max_length=25)
    postal_code = models.IntegerField()
    region = models.TextField(max_length=25)
    product_id = models.CharField(max_length=25)
    category = models.TextField(max_length=25)
    sub_category = models.TextField(max_length=25)
    product_name = models.CharField(max_length=200)
    sales = models.DecimalField(max_digits=10, decimal_places=5)
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=5)
    profit = models.DecimalField(max_digits=10, decimal_places=5)

