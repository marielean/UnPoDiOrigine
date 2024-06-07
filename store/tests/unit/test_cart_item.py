from django.test import TestCase
from store.models.product import Product
from store.models.customer import Customer
from store.models.cart_item import CartItem


class TestCartItem(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", price=100)
        self.customer = Customer.objects.create(first_name="Test", last_name="Customer", phone="1234567890", email="test@email.com", password="test123")
        self.cart_item = CartItem.objects.create(product=self.product, customer=self.customer, quantity=2)

    def test_create_cart_item(self):
        cart_item = CartItem.objects.create(product=self.product, customer=self.customer, quantity=1)
        self.assertEqual(cart_item.quantity, 1)
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.customer, self.customer)

    def test_update_cart_item(self):
        self.cart_item.quantity = 3
        self.cart_item.save()
        self.assertEqual(self.cart_item.quantity, 3)

    def test_get_total_price(self):
        total_price = self.cart_item.get_total_price()
        self.assertEqual(total_price, self.product.price * self.cart_item.quantity)

    def test_get_cart_by_customer(self):
        cart_items = CartItem.get_cart_by_customer(self.customer)
        self.assertIn(self.cart_item, cart_items)

    def test_get_cart_total_by_customer(self):
        total = CartItem.get_cart_total_by_customer(self.customer)
        self.assertEqual(total, self.product.price * self.cart_item.quantity)

    def test_create_cart_item_with_nonexistent_product_or_customer(self):
        with self.assertRaises(Exception):
            CartItem.objects.create(product=None, customer=self.customer, quantity=1)
        with self.assertRaises(Exception):
            CartItem.objects.create(product=self.product, customer=None, quantity=1)

    def test_get_total_price_after_product_price_or_quantity_change(self):
        self.product.price = 200
        self.product.save()
        self.cart_item.quantity = 3
        self.cart_item.save()
        total_price = self.cart_item.get_total_price()
        self.assertEqual(total_price, self.product.price * self.cart_item.quantity)

    def test_get_cart_by_customer_with_no_cart_items(self):
        customer = Customer.objects.create(first_name="Test 2", last_name="Customer", phone="1234567890", email="test2@email.com", password="test123")
        cart_items = CartItem.get_cart_by_customer(customer)
        self.assertEqual(cart_items.count(), 0)

    def test_get_cart_total_by_customer_with_no_cart_items(self):
        customer = Customer.objects.create(first_name="Test 2", last_name="Customer", phone="1234567890", email="test2@email.com", password="test123")
        total = CartItem.get_cart_total_by_customer(customer)
        self.assertEqual(total, 0)

    def test_get_cart_by_customer_with_nonexistent_customer(self):
        self.assertEqual(list(CartItem.get_cart_by_customer(None)), [])

    def test_get_cart_total_by_customer_with_nonexistent_customer(self):
        self.assertEqual(CartItem.get_cart_total_by_customer(None),0)