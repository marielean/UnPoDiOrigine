from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View
from store.models.form.signup_form import SignupForm

class Signup (View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'store/signup.html', {'form': form})
    
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            # Dati validi. Creare l'utente.
            Customer.objects.create_user(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect('homepage')
        else:
            # Dati non validi. Mostrare gli errori.
            return render(request, 'store/signup.html', {'form': form}, status=400)
