from django.test import TestCase
from store.models.customer import Customer, CustomerManager
from django.test import Client
from django.urls import reverse
from django.test import TestCase

class TestCustomer(TestCase):
    def setUp(self):
        self.manager = Customer.objects
        Customer.objects.create(first_name="John", last_name="Doe", phone="1234567890", email="john.doe@domain.com", password="password")

    def test_get_full_name(self):
        ''' Test if the full name of the customer is returned correctly '''
        customer = Customer.objects.get(email="john.doe@domain.com")
        full_name = customer.get_full_name()
        self.assertEqual(full_name, "John Doe")

    def test_update_customer(self):
        ''' Test if the customer details can be updated '''
        customer = Customer.objects.get(email="john.doe@domain.com")
        customer.first_name = "Updated"
        customer.last_name = "Name"
        customer.save()
        updated_customer = Customer.objects.get(email="john.doe@domain.com")
        self.assertEqual(updated_customer.first_name, "Updated")
        self.assertEqual(updated_customer.last_name, "Name")

    def test_delete_customer(self):
        ''' Test if the customer can be deleted '''
        customer = Customer.objects.get(email="john.doe@domain.com")
        customer.delete()
        with self.assertRaises(Customer.DoesNotExist):
            Customer.objects.get(email="john.doe@domain.com")

    def test_get_customer_by_email(self):
        ''' Test if the customer is fetched by email '''
        customer = Customer.get_customer_by_email("john.doe@domain.com")
        self.assertEqual(customer.first_name, "John")
        self.assertEqual(customer.last_name, "Doe")
        self.assertEqual(customer.phone, "1234567890")
        self.assertEqual(customer.email, "john.doe@domain.com")

    def test_create_user(self):
        ''' Test if the user is created '''
        customer = self.manager.create_user(email="test@email.com", first_name="Test", last_name="User", phone="1234567890", password="password")
        self.assertEqual(customer.first_name, "Test")
        self.assertEqual(customer.last_name, "User")
        self.assertEqual(customer.phone, "1234567890")
        self.assertEqual(customer.email, "test@email.com")
    
    def test_normalize_email(self):
        ''' Test if the email is normalized '''
        user = self.manager.create_user(email="Test@Example.COM", password="testpassword", first_name="Test", last_name="User", phone="1234567890")
        self.assertEqual(user.email, "Test@example.com")

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            self.manager.create_user(email=None, password="testpassword", first_name="Test", last_name="User", phone="1234567890")

    def test_create_superuser_without_is_staff(self):
        with self.assertRaises(ValueError):
            self.manager.create_superuser(email="admin@example.com", password="adminpassword", is_staff=False, first_name="Test", last_name="User", phone="1234567890")

    def test_create_superuser_without_is_superuser(self):
        with self.assertRaises(ValueError):
            self.manager.create_superuser(email="admin@example.com", password="adminpassword", is_superuser=False, first_name="Test", last_name="User", phone="1234567890")

    def test_password_set_correctly(self):
        user = self.manager.create_user(email="test@example.com", password="testpassword")
        self.assertNotEqual(user.password, "testpassword")
        self.assertTrue(user.check_password("testpassword"))