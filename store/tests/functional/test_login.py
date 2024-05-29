from django.test import TestCase
from django.urls import reverse
from store.models.customer import Customer

class LoginTestCase(TestCase):
    def setUp(self):
        self.email = 'test@email.com'
        self.password = 'testpassword'
        self.user = Customer.objects.create_user(
            first_name='John',
            last_name='Doe',
            phone='1234567890', 
            email=self.email,
            password=self.password
        )

    def test_login_success(self):
        login_url = reverse('login')
        response = self.client.post(login_url, {
            'email': self.email,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url, reverse('homepage'))
        self.assertTrue(self.user.is_authenticated)

    def test_login_failure(self):
        login_url = reverse('login')
        response = self.client.post(login_url, {
            'email': self.email,
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)

    def test_logout(self):
        self.client.login(email=self.email, password=self.password)

        logout_url = reverse('logout')
        response = self.client.get(logout_url)
        self.assertEqual(response.status_code, 302)
        # You should test that the user cannot access to a private page after logout