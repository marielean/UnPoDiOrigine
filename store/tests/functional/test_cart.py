from django.test import TestCase
from django.urls import reverse
from store.models.customer import Customer
from store.models.product import Product
from store.models.cart_item import CartItem

class CartTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(email='testuser@email.com', password='12345', first_name='Test', last_name='User', phone='1234567890')
        self.product = Product.objects.create(name='Test Product', price=10)

    def test_add_product_to_cart(self):
        self.client.login(email='testuser@email.com', password='12345')
        response = self.client.post(reverse('cart'), {'product_id': self.product.id, 'action': 'add'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CartItem.objects.filter(customer=self.customer, product=self.product).count(), 1)

    def test_remove_product_from_cart(self):
        CartItem.objects.create(customer=self.customer, product=self.product, quantity=1)
        self.client.login(email='testuser@email.com', password='12345')
        response = self.client.post(reverse('cart'), {'product_id': self.product.id, 'action': 'delete'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CartItem.objects.filter(customer=self.customer, product=self.product).count(), 0)

    def test_update_product_quantity_in_cart(self):
        CartItem.objects.create(customer=self.customer, product=self.product, quantity=1)
        self.client.login(email='testuser@email.com', password='12345')
        response = self.client.post(reverse('cart'), {'product_id': self.product.id, 'action': 'update', 'quantity': 2})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CartItem.objects.get(customer=self.customer, product=self.product).quantity, 2)

    def test_get_cart(self):
        # Create a cart
        self.cart_item = CartItem.objects.create(customer=self.customer, product=self.product, quantity=1)

        self.client.login(email='testuser@email.com', password='12345')
        response = self.client.get('/cart')  # replace with the actual path
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.cart_item.product.name)  # replace with actual product name