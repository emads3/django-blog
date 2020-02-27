from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from authentication.forms import Register
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    # count = User.objects.count()
    return render(request, 'djangoApp/adminpanel.html')

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Register()
    return render(request, 'authentication/registration/register.html',{
        'form':form
    })

# def my_view(request):
#     email = request.POST['email']
#     password = request.POST['password']
#     user = authenticate(request, email=email, password=password)
#     if user is not None:
#         login(request, user)
        
#     #else:
#         #return render(request'/authentication/home')