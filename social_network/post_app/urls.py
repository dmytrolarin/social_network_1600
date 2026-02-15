from django.urls import path
from .views import *

urlpatterns = [
    path(route = 'create/', view = render_create_post)
]
  
