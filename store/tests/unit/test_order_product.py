from django.test import TestCase
from store.models.product import Product
from store.models.customer import Customer
from store.models.order import Order
from store.models.order_product import OrderProduct

class TestOrderProduct(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price=100)
        self.customer = Customer.objects.create(first_name="Test", last_name="Customer", phone="1234567890", email="test@email.com", password="test123")
        self.order = Order.objects.create(customer=self.customer, address="Test Address", phone="1234567890", date="2021-01-01")
        self.order_product = OrderProduct.objects.create(order=self.order, product=self.product, quantity=2)

    def test_order_product_creation(self):
        self.assertEqual(self.order_product.order, self.order)
        self.assertEqual(self.order_product.product, self.product)
        self.assertEqual(self.order_product.quantity, 2)

    def test_order_product_update_quantity(self):
        new_quantity = 3
        self.order_product.quantity = new_quantity
        self.order_product.save()
        self.assertEqual(self.order_product.quantity, new_quantity)