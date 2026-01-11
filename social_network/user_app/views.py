from django.shortcuts import render, redirect
from django.http import HttpRequest 
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout


def render_registration(request: HttpRequest):
    context = {'error': ' '}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            try:
                User.objects.create_user(username= username, password= password)
                return redirect("login")
            except IntegrityError:
                context['error'] = "Такий користувач вже iснує"
        else:
            context['error'] = "Паролі не співпадають"
    return render(
        request= request, 
        template_name= 'user_app/registration.html', 
        context= context
        )


def render_login(request: HttpRequest):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request=request, username= username, password= password)
       
        if user != None:
            login(request, user)
            return redirect("welcome")
        else:
            context['error'] = "Невірний логін або пароль"

    return render(
        request = request, 
        template_name= 'user_app/login.html',
        context=context
        )

def render_welcome(request: HttpRequest):
    if request.user.is_authenticated:
        return render(
            request= request, 
            template_name= "user_app/welcome.html", 
            )
    else:
        return redirect("login")
    
    
def logout_user(request: HttpRequest):
    logout(request)
    return redirect("login")


def render_admin(request: HttpRequest):
    if request.user.username != 'admin':
        return redirect('login')
    else:
        return render(request, 'user_app/admin.html')