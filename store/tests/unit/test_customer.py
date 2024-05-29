from django.test import TestCase
from store.models.customer import Customer
from django.test import Client
from django.urls import reverse
from django.test import TestCase

class TestCustomer(TestCase):
    def setUp(self):
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
        self.assertEqual(customer.password, "password")

    def test_isExists(self):
        ''' Test if the customer exists '''
        customer = Customer.objects.get(email="john.doe@domain.com")
        self.assertTrue(customer.isExists())

        another_customer = Customer(first_name="Jane", last_name="Doe", phone="0987654321", email="jane.doe@domain.com", password="password")
        self.assertFalse(another_customer.isExists())

    # It is not necessary to delete the objects created in the setUp method since the test database is destroyed after the tests are run.
    # def tearDown(self):
    #     Customer.objects.all().delete()
        
    