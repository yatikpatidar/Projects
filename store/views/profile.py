from django.shortcuts import render , redirect
from django.views import View
from ..models.customer import Customer
from django.http import HttpResponse

class Profile(View):
    def get(self ,request) :

        email = request.session.get('email')
        # print("profile id " ,request.session.get('id'))
        customer_detail = Customer.get_customer_by_email(email = email)

        # print("value aa gai idhr side 1 " , request.GET.get('toggle_content') )
        show_content = False
        val = request.GET.get('toggle_content') == 'true'
        if val :
           show_content = True
           
        if customer_detail :
            customer = {
                
                'first_name': customer_detail.first_name , 
                'last_name': customer_detail.last_name ,
                'phone': customer_detail.phone ,
                'email': customer_detail.email ,
                'img':  customer_detail.image,
                'password': customer_detail.password 
                
            }
            return render(request , "profile.html" , {'customer' : customer , 'values':customer ,'show_content':show_content})

        else :
            # we never come on this condition because we already login
            return redirect('login')
        

    def post(self , request):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        prev_email = request.POST.get('prev_email')
        password= request.POST.get('password')

        customer_profile = Customer.get_customer_by_email(email = prev_email)
        print("password " , password)

        # validation
        error_message = ''

        if (not firstname):
            error_message = "First name Required !"
        elif len(firstname) < 4:
            error_message = "Length of First Name should be 4 or more char"
        elif (not lastname):
            error_message = "Last name Required !"
        elif len(lastname) < 4:
            error_message = "Length of Last Name should be 4 or more char"
        elif (not phone):
            error_message = "Phone number Required !"
        elif len(phone) <10:
            error_message = "phone number must be 10 digit"
        elif (not password):
            error_message = "Password required"
        elif len(password) < 6:
            error_message = "minimum length should be 6 char"
        
        if error_message :
            value = {
            # 'show_content':True,
            'first_name':firstname,
            'last_name':lastname ,
            'phone' : phone ,
            'email': prev_email
        }
            print("not open idhr open hori kya " , customer_profile.image.url)
            data = {
                'show_content':True,
                'error':error_message,
                'values':value,
                'customer':customer_profile
            }
            return render(request , 'profile.html' , data )

        if request.FILES.get('profile_image') :
            customer_profile.image = request.FILES.get('profile_image')
        
        customer_profile.first_name = firstname
        customer_profile.last_name = lastname
        customer_profile.phone = phone
        if request.POST.get('new_email') : 
            customer_profile.email = request.POST.get('new_email')

        customer_profile.save()

        # data = {
        #     'show_content':False,
        #     'values':customer_profile

        # }

        # return render(request , 'profile.html' , data )
        return redirect('profile')
    