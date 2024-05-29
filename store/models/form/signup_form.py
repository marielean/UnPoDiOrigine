from django import forms
from store.models.customer import Customer

class SignupForm(forms.Form):
    first_name = forms.CharField(min_length=3, max_length=255, required=True, label='First Name')
    last_name = forms.CharField(min_length=3, max_length=255, required=True, label='Last Name')
    phone = forms.CharField(max_length=255, required=True, label='Phone Number')
    email = forms.EmailField(max_length=255, required=True, label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput, required=True, label='Password')

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("First Name Required")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last Name Required")
        return last_name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError("Phone Number Required")
        return phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Password Required")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email Required")
        elif Customer.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Address Already Registered")
        return email