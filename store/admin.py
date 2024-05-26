from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)

# Register your models here.