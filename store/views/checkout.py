from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.order import Order
from store.models.order_product import OrderProduct
from store.models.cart_item import CartItem
import datetime
from django.db import transaction
from store.models.form.checkout_form import CheckoutForm

class CheckOut(View):
    def get(self, request):
        form = CheckoutForm()
        customer = request.user
        cart = CartItem.get_cart_by_customer(customer)
        total = CartItem.get_cart_total_by_customer(customer)
        return render(request, 'store/checkout.html', {'form': form, 'cart': cart, 'total': total})

    @transaction.atomic
    def post(self, request):
        form = CheckoutForm(request.POST)
        customer = request.user
        cart = CartItem.get_cart_by_customer(customer)

        if not form.is_valid():
            return render(request, 'store/checkout.html', {'form': form, 'cart': cart})
        
        order = Order(customer=customer,
                          address=form.data.get('address'),
                          phone=form.data.get('phone'),
                          date=datetime.datetime.today()
                          )
        order.save()

        for cart_item in cart:
            # create order product
            order_product = OrderProduct(order=order,
                                         product=cart_item.product,
                                         quantity=cart_item.quantity
                                         )
            order_product.save()
            # delete cart item
            cart_item.delete()
            
        return redirect('orders')