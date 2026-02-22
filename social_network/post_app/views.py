from django.shortcuts import render
from .models import Tag


# Create your views here.
def render_create_post(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        print(request.POST)
    return render(
        request, 
        "post_app/create_post.html",
        context={'tags': tags}
        )
    

