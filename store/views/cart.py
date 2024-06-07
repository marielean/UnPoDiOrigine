from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Product
from store.models.cart_item import CartItem

class Cart(View):
    def get(self, request):
        cart = CartItem.get_cart_by_customer(request.user)
        total = CartItem.get_cart_total_by_customer(request.user)
        return render(request, 'store/cart.html', {'cart': cart, 'total': total})

    def post(self, request):
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        product = Product.objects.get(id=product_id)
        if action == 'add':
            if CartItem.objects.filter(customer=request.user, product=product).exists():
                cart_item = CartItem.objects.get(customer=request.user, product=product)
                cart_item.quantity += 1
                cart_item.save()
            else:
                CartItem.objects.get_or_create(customer=request.user, product=product)            
        elif action == 'update':
            quantity = request.POST.get('quantity')
            cart_item = CartItem.objects.get(customer=request.user, product=product)
            cart_item.quantity = quantity
            cart_item.save()
        elif action == 'delete':
            CartItem.objects.filter(customer=request.user, product=product).delete()
        return redirect('cart')