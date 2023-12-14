from django.shortcuts import render , redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from django.http import HttpResponseRedirect

class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')
    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email , password)
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password , customer.password)
            
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = email

                print(request.session.get('email'))

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            
            else:
                error_message = ' Password is invalid !! '
                
        else:
            error_message = 'Email is invalid !! '
        # print(customer)
        # print(email , password)

        return render(request , 'login.html' , {'error':error_message})


def logout(request):
    request.session.clear()
    return redirect('login')