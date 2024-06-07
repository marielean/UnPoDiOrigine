from django.test import TestCase, Client
from django.urls import reverse
from store.models.cart_item import CartItem
from store.models.form.checkout_form import CheckoutForm
from store.models.product import Product
from store.models.customer import Customer

class CheckoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Customer.objects.create_user(email='test@email.com', password='12345', first_name='Test', last_name='User', phone='1234567890')
        self.product = Product.objects.create(name='Test Product', price=100)
        self.cart_item = CartItem.objects.create(customer=self.user, product=self.product , quantity=1) 

    def test_get_checkout(self):
        self.client.login(email='test@email.com', password='12345')
        response = self.client.get(reverse('checkout'))  # replace 'checkout' with the actual name of the checkout view
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')  # replace with actual form context variable
        self.assertContains(response, 'cart')  # replace with actual cart context variable
        self.assertContains(response, 'total')  # replace with actual total context variable

    def test_post_checkout(self):
        self.client.login(email='test@email.com', password='12345')
        form = CheckoutForm({
            'address': '123 Test St',
            'phone': '1234567890',
            'card_number': '1234567890123456',
        })
        response = self.client.post(reverse('checkout'), data=form.data)
        self.assertRedirects(response, reverse('orders')) 