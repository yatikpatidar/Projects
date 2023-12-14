from django.shortcuts import render , redirect
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from django.contrib.auth.hashers import make_password , check_password
from django.views import View
# Create your views here.

class Index(View):
    def get(self , request):
        # product = Product.get_all_product()
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}


        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        
        if category_id:
            product = Product.get_all_products_by_category_id(category_id)
        else:
            product = Product.get_all_product()
        data = {}
        data['products'] = product
        data['categories'] = categories

        print('you are ' , request.session.get('email'))
        return render(request , 'index.html' , data )

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')

        cart = request.session.get('cart')

        if cart :
            quantity = cart.get(product)
            if quantity :
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart
        print(request.session['cart'])


        return redirect('homepage')