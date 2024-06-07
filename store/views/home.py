from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.template import loader

class Index(View):    
    def get(self, request):
        # return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
        # product_list = Product.get_all_products()
        # context = {"product_list": product_list}
        
        # return render(request, 'store/index.html', context)
        return self.__store(request)
    
    def __store(self, request):
        # cart = request.session.get('cart')
        # if not cart:
        #     request.session['cart'] = {}
        # products = None
        # categories = Category.get_all_categories()
        # categoryID = request.GET.get('category')
        # if categoryID:
        #     products = Product.get_all_products_by_categoryid(categoryID)
        # else:
        #     products = Product.get_all_products()
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = Product.get_all_products()
        categories = Category.get_all_categories()


        data = {}
        data['products'] = products
        data['categories'] = categories

        print('you are:', request.session.get('email'))
        return render(request, 'store/index.html', data)