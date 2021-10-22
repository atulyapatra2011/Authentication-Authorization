from django.shortcuts import redirect, render ,redirect
from django.contrib.auth.models import User
from app.forms import Registration_Form,Login_Form
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password

# Create your views here.


def SignUp(request):
    if request.method == "POST":
        signup = Registration_Form(request.POST or None)
        if signup.is_valid():
            try:
                first_name = request.POST['First_Name']
                last_name = request.POST['Last_Name']
                email = request.POST['email']
                username = request.POST['username']
                password = request.POST['password']

                signup_data = User.objects.create(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
                if signup_data:
                    signup_data.password = make_password(signup_data.password)
                    signup_data.save()
                    messages.success(request,'Successfully data register..')
                else:
                    messages.error(request,'give me valid information..')
                signup = Registration_Form()
                signupitems = User.objects.values
                print(signupitems)
            except Exception as b:
                print(b)
                messages.error(request,f'something Wrong {b}'.format(b))

    else:
        signup = Registration_Form()
    dict = {'signup':signup}
    return render(request,'myapp/SignUp.html',dict)


def user_login(request):
    if request.method == "POST":
        login_data = Login_Form(request.POST or None)
        if login_data.is_valid():
            try:
                UserName = request.POST['username']
                Password = request.POST['password']
                
                user = authenticate(request,username=UserName,password=Password)
                print(user)
                if user is not None:
                    if user.is_authenticated and user.is_staff:                    
                        login(request,user)
                        messages.success(request,'Succesfully Login')
                        return redirect(reverse('home')) 
                    else:
                        messages.error(request,'User is not Authenticated')          
                else:
                    messages.error(request,'UserName and Password is Incorrect')
            except Exception as b:
                print(b)
                messages.error(request,f'something Wrong {b}'.format(b))
    else:
        login_data = Login_Form()
    dict = {'login':login_data}
    return render(request,'myapp/login.html',dict)


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def home(request):
    return render(request,'myapp/home.html')


def user_delete(request,id):
    if request.method == "GET":
        user = User.objects.get(id=id)
        user.delete()
        messages.success(request,'Successfully Delete user data')
    else:
        messages.warning(request,'Unable to Delete user data')
    return redirect(reverse('user_list'))

def view_users(request):
    if request.method == "GET":
        users = User.objects.order_by('id').all()
    else:
        messages.warning(request,'Data Not Found')
    dict = {'user':users}
    return render(request,'myapp/users.html',dict)