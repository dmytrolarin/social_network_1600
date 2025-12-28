from django.urls import path
from .views import *


urlpatterns= [
    path(route= "registration/", view= render_registration, name= "registration"),
    path(route= "login/", view= render_login, name= "login"),
    path(route= "welcome/", view= render_welcome, name= "welcome"),
    path(route= "logout/", view= logout_user, name= "logout")
]