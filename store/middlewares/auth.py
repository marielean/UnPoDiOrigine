from django.shortcuts import redirect
from django.contrib.auth import get_user


def auth_middleware(get_response):

    def middleware(request):
        user = get_user(request)
        if not user.is_authenticated:
            return redirect('login')
        
        response = get_response(request)

        return response
    
    return middleware