from django.shortcuts import render , redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password 
from django.views import View


class Signup(View):
    def get(self , request):

        return render(request , 'signup.html')
    
    def post(self , request):
        postdata = request.POST
        firstname = postdata.get('firstname')
        lastname = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        # checking for image upload or not
        if request.FILES.get('profile_image') :
            img = request.FILES.get('profile_image')
            print("profile image " ,img)
            customer = Customer(first_name = firstname ,
                                    last_name = lastname ,
                                    phone = phone ,
                                    email = email ,
                                    password = password,
                                    image = img  )
        else:
            # print("profile image " ,img)
            customer = Customer(first_name = firstname ,
                                    last_name = lastname ,
                                    phone = phone ,
                                    email = email ,
                                    password = password,
                                   )
            
        # kwargs = {
        #     'name': name,
        #     'email': email,
        # }

        # # Add the profile_image to kwargs if it is provided
        # if profile_image:
        #     kwargs['profile_image'] = profile_image

        # # Create the UserProfile instance with the provided or default values
        # user_profile = UserProfile(**kwargs)
        
        value = {
            'firstname':firstname,
            'lastname':lastname ,
            'phone' : phone ,
            'email': email
        }
        
        error_message = self.validateCustomer(customer)

        if  not error_message:
            print(firstname , lastname , phone , email , password)
            customer.password = make_password(customer.password)

            customer.register()
        
            return redirect('homepage')
        else:
            data = {
                'error':error_message,
                'values':value
            }
            return render(request , 'signup.html' , data)
        
    def validateCustomer(self ,customer):
        error_message = ''

        if (not customer.first_name):
            error_message = "First name Required !"
        elif len(customer.first_name) < 4:
            error_message = "Length of First Name should be 4 or more char"
        elif (not customer.last_name):
            error_message = "Last name Required !"
        elif len(customer.last_name) < 4:
            error_message = "Length of Last Name should be 4 or more char"
        elif (not customer.phone):
            error_message = "Phone number Required !"
        elif len(customer.phone) <10:
            error_message = "phone number must be 10 digit"
        elif (not customer.password):
            error_message = "Password required"
        elif len(customer.password) < 6:
            error_message = "minimum length should be 6 char"
        elif customer.isExists():
            error_message = "Email Address Already Registered "

        return error_message
 
