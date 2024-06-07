from django.test import TestCase
from store.models.form.signup_form import SignupForm
from store.models.customer import Customer

class TestSignupForm(TestCase):
    def test_clean_email_valid(self):
        form = SignupForm(data={'email': 'test@example.com'})
        form.is_valid()
        self.assertEqual(form.cleaned_data['email'], 'test@example.com')

    def test_clean_email_required(self):
        form = SignupForm(data={'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_clean_email_already_registered(self):
        # Create a customer with the email address
        Customer.objects.create(
            first_name="John", 
            last_name="Doe", 
            phone="1234567890", 
            email="test@example.com",
            password="password123"
            )

        form = SignupForm(data={
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone': '1234567890',
            'password': 'password123'
            })
        form.is_valid()
        self.assertIn('email', form.errors)

    def test_clean_first_name(self):
        form = SignupForm(data={'first_name': 'John'})
        form.is_valid()
        self.assertEqual(form.cleaned_data['first_name'], 'John')

    def test_clean_first_name_min_length(self):
        form = SignupForm(data={'first_name': 'Jo'})
        form.is_valid()
        self.assertIn('first_name', form.errors)

    def test_clean_last_name(self):
        form = SignupForm(data={'last_name': 'Doe'})
        form.is_valid()
        self.assertEqual(form.cleaned_data['last_name'], 'Doe')

    def test_clean_last_name_min_length(self):
        form = SignupForm(data={'last_name': 'Do'})
        form.is_valid()
        self.assertIn('last_name', form.errors)

    def test_clean_phone(self):
        form = SignupForm(data={'phone': '1234567890'})
        form.is_valid()
        self.assertEqual(form.cleaned_data['phone'], '1234567890')

    def test_clean_password(self):
        form = SignupForm(data={'password': 'password123'})
        form.is_valid()
        self.assertEqual(form.cleaned_data['password'], 'password123')