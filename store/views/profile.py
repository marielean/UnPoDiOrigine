from django.shortcuts import render, redirect
from django.views import View
from store.models.form.user_profile_form import UserProfileForm

class Profile(View):
    def get(self, request):
        form = UserProfileForm(instance=request.user)
        return render(request, 'store/profile.html', {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'store/profile.html', {'form': form})