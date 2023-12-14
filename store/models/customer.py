from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/profile_img/' , default="uploads/profile_img/download.jfif" )

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False 

    @staticmethod
    def get_detail(self):
        customer_d = Customer.objects.get(id = self)
        name = customer_d.first_name
        print(customer_d)
        print(name)
        return name
        # return "yatiik ruk ja abhi"

    @staticmethod
    def get_detail_image(self):
        customer_d = Customer.objects.get(id = self)
        img = customer_d.image
        print(customer_d)
        return img

