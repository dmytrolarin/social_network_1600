from django.urls import path
from .views import render_registration


urlpatterns= [
    path(route= "registration/", view= render_registration, name= "registration")
]