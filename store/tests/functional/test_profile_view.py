from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from store.models.customer import Customer

class ProfileViewTests(TestCase):
    def setUp(self):
        # Creazione e login dell'utente di test
        self.user = Customer.objects.create_user(email='testuser@email.com', password='12345', first_name='Test', last_name='User', phone='1234567890')
        self.client.login(email='testuser@email.com', password='12345')

    def test_profile_view_get(self):
        # Test per la GET request
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'form')

    def test_profile_view_post_success(self):
        # Test per la POST request con dati validi
        response = self.client.post(reverse('profile'), {'first_name': 'Test', 'last_name': 'User'})
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Test')

    def test_profile_view_post_failure(self):
        # Test per la POST request con dati non validi
        response = self.client.post(reverse('profile'), {'first_name': '', 'last_name': ''})
        # self.assertNotEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'first_name', 'This field is required.')
