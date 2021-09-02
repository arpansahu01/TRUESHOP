from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegdForm,LoginForm
from django.contrib import messages


# def home(request):
#  return render(request, 'app/home.html')
class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobile':mobiles,'laptop':laptops})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class productDetailview(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

# def add_to_cart(request):
#  return render(request, 'app/addtocart.html')
class AddcartView(View):
    def get(self,request):
        return render(request,'app/addtocart.html')

# def buy_now(request):
#  return render(request, 'app/buynow.html')
class BuynowView(View):
    def get(self,request):
        return render(request,'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')
class ProfileView(View):
    def get(self,request):
        return render(request,'app/profile.html')

# def address(request):
#  return render(request, 'app/address.html')
class AddressView(View):
    def get(self,request):
        return render(request,'app/address.html')

# def orders(request):
#  return render(request, 'app/orders.html')
class OdersView(View):
    def get(self,request):
        return render(request,'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')
# class ChangePasswordView(View):
#     def get(self,request):
#         return render(request,'app/changepassword.html')

# def mobile(request):
#  return render(request, 'app/mobile.html')
class MobileView(View):
    def get(self,request,data=None):
        if data == None:
            mobile = Product.objects.filter(category='M')
        elif data == 'apple' or data == 'oneplus':
            mobile = Product.objects.filter(category='M').filter(brand=data) 
        elif data == 'below':
            mobile = Product.objects.filter(category='M').filter(discount_price__lt=6000)
        elif data == 'above':
            mobile = Product.objects.filter(category='M').filter(discount_price__gt=6000)                   
        return render(request,'app/mobile.html',{'mobile':mobile})

# def login(request):
#  return render(request, 'app/login.html')
# class LoginView(View):
#     def get(self,request):
#         form = LoginForm()
#         return render(request,'app/login.html',{'form':form}) 
#     def post(self,request):
#         form = LoginForm(request.POST)
#         user = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         if (user == 'username' | password == 'password'):
#             return HttpResponseRedirect('/')
               

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class CustRegdView(View):
    def get(self,request):
        form = CustomerRegdForm()
        return render(request,'app/customerregistration.html',{'form':form})
    def post(self,request):
        form = CustomerRegdForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations!! Regeistered Succesfully")
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})    
         


# def checkout(request):
#  return render(request, 'app/checkout.html')
class CheckoutView(View):
    def get(self,request):
        return render(request,'app/checkout.html')
