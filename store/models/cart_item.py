from django.db import models
from .product import Product
from .customer import Customer

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
    
    @staticmethod
    def get_cart_total_by_customer(customer_id):
        cart_items = CartItem.objects.filter(customer = customer_id)
        total = 0
        for cart_item in cart_items:
            total += cart_item.get_total_price()
        return total
    
