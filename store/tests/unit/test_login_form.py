from django.test import TestCase
from store.models.form.login_form import LoginForm
from store.models.customer import Customer

class TestLoginForm(TestCase):
    def setUp(self):
        self.user = Customer.objects.create_user(
            email='test@example.com', 
            password='testpassword',
            first_name='Test',
            last_name='User',
            phone='1234567890'
            )

    def test_valid_login(self):
        form_data = {'email': 'test@example.com', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_login(self):
        form_data = {'email': 'test@example.com', 'password': 'wrongpassword'}
        form = LoginForm(form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['__all__'], ['Invalid email or password'])

    def test_missing_email(self):
        form_data = {'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])

    def test_missing_password(self):
        form_data = {'email': 'test@example.com'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])

    def test_invalid_email_format(self):
        form_data = {'email': 'testexample.com', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])