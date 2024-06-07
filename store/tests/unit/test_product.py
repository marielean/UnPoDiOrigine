from django.test import TestCase
from store.models.product import Product
from store.models.category import Category

class TestProduct(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Category 1")
        self.category2 = Category.objects.create(name="Category 2")
        self.product1 = Product.objects.create(name="Test Product 1", price=10.0, category=self.category1)
        self.product2 = Product.objects.create(name="Test Product 2", price=20.0, category=self.category1)
        self.product3 = Product.objects.create(name="Test Product 3", price=30.0, category=self.category2)

    def test_get_products_by_id(self):
        products = Product.get_products_by_id([self.product1.id, self.product3.id])
        self.assertEqual(products.count(), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product3, products)

    def test_get_all_products(self):
        products = Product.get_all_products()
        self.assertEqual(products.count(), 3)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)
        self.assertIn(self.product3, products)

    def test_get_all_products_by_categoryid(self):
        products = Product.get_all_products_by_categoryid(self.category1.id)
        self.assertEqual(products.count(), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)

    def test_product_creation(self):
        self.assertEqual(self.product1.name, "Test Product 1")
        self.assertEqual(self.product1.price, 10.0)
        self.assertEqual(self.product1.category, self.category1)