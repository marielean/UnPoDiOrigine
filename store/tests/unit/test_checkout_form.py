from django.test import TestCase
from store.models.form.checkout_form import CheckoutForm

class TestCheckoutForm(TestCase):
    def test_form_valid_data(self):
        form = CheckoutForm({
            'address': '123 Test Street',
            'phone': '1234567890',
            'card_number': '1234123412341234'
        })
        self.assertTrue(form.is_valid())
    
    def test_form_missing_required_fields(self):
        form = CheckoutForm({
            'address': '',
            'phone': '',
            'card_number': ''
        })
        self.assertFalse(form.is_valid())

    def test_form_invalid_phone_format(self):
        form = CheckoutForm({
            'address': '123 Test Street',
            'phone': 'invalidphone',
            'card_number': '1234123412341234'
        })
        self.assertFalse(form.is_valid())
    
    def test_form_card_number_length(self):
        form = CheckoutForm({
            'address': '123 Test Street',
            'phone': '1234567890',
            'card_number': '1234'
        })
        self.assertFalse(form.is_valid())