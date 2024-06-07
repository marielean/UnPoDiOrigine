from django import forms

class CheckoutForm(forms.Form):
    address = forms.CharField(max_length=200, required=True, widget=forms.Textarea(attrs={'rows': 3}), label='Address')
    phone = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone'}), label='Phone')
    card_number = forms.CharField(max_length=16, required=True, widget=forms.TextInput(attrs={'placeholder': 'Card Number'}), label='Card Number')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.isdigit():
            raise forms.ValidationError('Invalid phone number')
        
        if len(phone) < 10:
            raise forms.ValidationError('Phone number must be at least 10 digits')
        
        if len(phone) > 15:
            raise forms.ValidationError('Phone number must be at most 15 digits')
        
        return phone
    
    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if not card_number.isdigit():
            raise forms.ValidationError('Invalid card number')
        
        if len(card_number) != 16:
            raise forms.ValidationError('Card number must be 16 digits')
        return card_number
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    