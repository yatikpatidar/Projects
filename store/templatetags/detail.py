from django import template
from store.models.customer import Customer
register = template.Library()

@register.filter(name = "login_detail")
def login_detail(customer):
    print("this is a customer " ,customer)
    # print(customer.email)
    name = Customer.get_detail(customer)
    return name

@register.filter(name = "login_detail_image")
def login_detail_image(customer):
    img = Customer.get_detail_image(customer)
    print("profile img " ,img)
    return img.url
    

