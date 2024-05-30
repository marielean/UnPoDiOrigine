from django.db import models
from .product import Product
from .customer import Customer
import datetime

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def placeCartItem(self):
        self.save()

    @staticmethod
    def get_cart_by_customer(customer_id):
        return CartItem.objects.filter(customer = customer_id)
    
    def get_total_price(self):
        return self.product.price * self.quantity