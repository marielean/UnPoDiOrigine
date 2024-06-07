from django.test import TestCase
from django.urls import reverse
from store.models.customer import Customer

class OrdersViewTest(TestCase):
    def setUp(self):
        test_customer = Customer.objects.create_user(first_name='Test', last_name='User', phone='1234567890', email='testuser@example.com', password='12345')
        self.client.login(email='testuser@example.com' , password='12345')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/orders')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('orders'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('orders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/orders.html')
        