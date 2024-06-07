from django.shortcuts import redirect
from django.contrib.auth import get_user
from django.urls import reverse


def auth_middleware(get_response):

    def middleware(request):
        user = get_user(request)
        login_url = reverse('login')
        if not user.is_authenticated and request.path != login_url:
            return redirect('login')
        
        response = get_response(request)
        return response
    
    return middleware