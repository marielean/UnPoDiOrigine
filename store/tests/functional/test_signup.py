from django.test import TestCase
from store.models.customer import Customer
from django.test import TestCase

class TestSignup(TestCase):
    def test_signup_with_invalid_data(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'email': 'invalid_email',
            'password': 'password123'
        }
        response = self.client.post('/signup', data=form_data)
        self.assertEqual(response.status_code, 400)  # Stay on the same page
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_signup_with_existing_email(self):
        Customer.objects.create(
            first_name="Existing",
            last_name="User",
            phone="0987654321",
            email="existing@example.com",
            password="password123"
        )
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'email': 'existing@example.com',
            'password': 'password123'
        }
        response = self.client.post('/signup', data=form_data)
        # self.assertEqual(response.status_code, 400)  # Stay on the same page
        self.assertFormError(response, 'form', 'email', 'Email Address Already Registered')
    
    def test_signup_with_valid_data(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'email': 'test@example.com',
            'password': 'password123'
        }
        response = self.client.post('/signup', data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful signup
        self.assertTrue(Customer.objects.filter(email='test@example.com').exists())

    def test_signup_page_display(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'store/signup.html')