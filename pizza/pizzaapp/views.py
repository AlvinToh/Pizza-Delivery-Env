from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PizzaModel
# Create your views here.


def adminloginview(request):
    return render(request, "pizzaapp/adminlogin.html")


def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    # user exists
    if user is not None and user.username == "admin":
        login(request, user)
        return redirect('adminhomepage')

    # user doesnt exists
    if user is None:
        messages.add_message(request, messages.ERROR, "Invalid credentials")
        return redirect('adminloginpage')


def adminhomepageview(request):
    context = {'pizzas': PizzaModel.objects.all()}
    return render(request, "pizzaapp/adminhomepage.html", context)


def adminlogout(request):
    logout(request)
    return redirect('adminloginpage')


def addpizza(request):
    # write a code to add the pizza into the database
    name = request.POST['pizza']
    price = request.POST['price']
    PizzaModel(name=name, price=price).save()
    return redirect('adminhomepage')
