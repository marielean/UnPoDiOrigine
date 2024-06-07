from django.test import TestCase
from store.models.product import Product
from store.models.customer import Customer
from store.models.order import Order
from store.models.order_product import OrderProduct

class TestOrder(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(first_name="Test", last_name="Customer", phone="1234567890", email="test@email.com", password="test123")
        self.order = Order.objects.create(customer=self.customer, address="Test Address", phone="1234567890", date="2021-01-01")
        self.product = Product.objects.create(name="Test Product", price=10.0)

    def test_order_creation(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.address, "Test Address")
        self.assertEqual(self.order.phone, "1234567890")
        self.assertEqual(self.order.date, "2021-01-01")

    def test_order_update_address(self):
        new_address = "New Test Address"
        self.order.address = new_address
        self.order.save()
        self.assertEqual(self.order.address, new_address)

    def test_order_deletion(self):
        self.order.delete()
        self.assertEqual(Order.objects.filter(id=self.order.id).count(), 0)

    def test_order_with_products(self):
        product = Product.objects.create(name="Test Product B", price=10.0)
        OrderProduct.objects.create(order=self.order, product=product, quantity=2)
        self.assertEqual(self.order.get_total_price(), 20.0)

    def test_get_orders_by_customer(self):
        orders = Order.get_orders_by_customer(self.customer.id)
        self.assertEqual(orders.count(), 1)
        self.assertEqual(orders.first(), self.order)

    def test_get_products(self):
        OrderProduct.objects.create(order=self.order, product=self.product, quantity=2)
        products = self.order.get_products()
        self.assertEqual(products.count(), 1)
        self.assertEqual(products.first(), self.product)

    def test_get_order_products(self):
        order_product = OrderProduct.objects.create(order=self.order, product=self.product, quantity=2)
        order_products = self.order.get_order_products()
        self.assertEqual(order_products.count(), 1)
        self.assertEqual(order_products.first(), order_product)

    def test_get_total_price(self):
        OrderProduct.objects.create(order=self.order, product=self.product, quantity=2)
        self.assertEqual(self.order.get_total_price(), 20.0)