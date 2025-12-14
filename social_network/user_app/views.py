from django.shortcuts import render
from django.http import HttpRequest 
from django.contrib.auth.models import User


# Create your views here. 
def render_registration(request: HttpRequest):
    context = {'error': ' '}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
           User.objects.create_user(username= username, password= password)
        else:
            context['error'] = "Паролі не співпадають"
    return render(request= request, template_name= 'user_app/registration.html', context= context)