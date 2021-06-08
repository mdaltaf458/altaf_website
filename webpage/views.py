from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'webpage/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'webpage/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentproducts')
            except IntegrityError:
                return render(request, 'webpage/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'webpage/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'webpage/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'webpage/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currentproducts')

@login_required()
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required()
def currentproducts(request):
    prods = Product.objects.filter(user=request.user)
    return render(request, 'webpage/currentproducts.html', {'prods': prods})

@login_required()
def createproduct(request):
    if request.method == 'GET':
        return render(request,'webpage/createproduct.html', {'form':ProductForm()})
    else:
        try:
            form = ProductForm(request.POST)
            newproduct = form.save(commit=False)
            newproduct.user = request.user
            newproduct.save()
            return redirect('currentproducts')
        except ValueError:
            return render(request, 'webpage/createproduct.html', {'form': ProductForm(),'error':'Bad data passes size of title exceeded'})

@login_required()
def viewproduct(request, product_pk):
    prods = get_object_or_404(Product,pk=product_pk,user=request.user)
    if request.method=='GET':
        form=ProductForm(instance=prods)
        return render(request, 'webpage/viewproduct.html', {'prods': prods,'form':form})
    else:
       form = ProductForm(request.POST,instance=prods)
       form.save()
       return redirect('currentproducts')