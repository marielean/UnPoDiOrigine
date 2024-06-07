from django.test import TestCase
from django.urls import reverse
from django.test import Client
from store.models.customer import Customer
from store.models.product import Product


class HomeViewTest(TestCase):
    pass
    def setUp(self):
        self.client = Client()
        self.user = Customer.objects.create_user(email='test@email.com', password='12345', first_name='Test', last_name='User', phone='1234567890')
        self.product = Product.objects.create(name='Test Product', price=100)

    def test_home_page_display(self):
        response = self.client.get(reverse('homepage')) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/index.html')