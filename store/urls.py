from django.contrib import admin
from django.urls import path
from .views import *
from .middlewares.auth import auth_middleware

urlpatterns = [
    path("", Index.as_view(), name="homepage"),
    # path('store', Store.as_view(), name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('checkout', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders')
    # path('cart', auth_middleware(Cart.as_view()), name='cart'),
]