from django.db import models
from .customer import Customer
from .product import Product
import datetime

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=255, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    products = models.ManyToManyField(Product, through='OrderProduct')

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')
    
    def get_products(self):
        return self.products.all()
    
    def get_order_products(self):
        return self.orderproduct_set.all()
    
    def get_total_price(self):
        order_products = self.get_order_products()
        total = 0
        for order_product in order_products:
            total += order_product.product.price * order_product.quantity
        return total
