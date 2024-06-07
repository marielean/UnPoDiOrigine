from django.test import TestCase
from store.models.customer import Customer
from store.models.form.user_profile_form import UserProfileForm

class TestUserProfileForm(TestCase):
    def setUp(self):
        self.user = Customer.objects.create_user(
            first_name='Test',
            last_name='User',
            phone='1234567890',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_form_valid(self):
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'phone': '1234567890',
            'new_password': 'newpassword',
            'confirm_password': 'newpassword'
        }, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_form_password_mismatch(self):
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'phone': '1234567890',
            'new_password': 'newpassword',
            'confirm_password': 'wrongpassword'
        }, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['new_password'], ['Le password non corrispondono'])

    def test_form_missing_fields(self):
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'User',
            'email': '',
            'phone': '1234567890',
            'new_password': 'newpassword',
            'confirm_password': 'newpassword'
        }, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_form_invalid_email(self):
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'invalidemail',
            'phone': '1234567890',
            'new_password': 'newpassword',
            'confirm_password': 'newpassword'
        }, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_save_commit_false(self):
        form = UserProfileForm({
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'phone': '1234567890',
            'new_password': 'newpassword',
            'confirm_password': 'newpassword'
        }, instance=self.user)
        user = form.save(commit=False)
        self.assertIsNone(user)
