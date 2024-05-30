from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(CartItem)

# Register your models here.