from django.shortcuts import render

# Create your views here.
def render_create_post(request):
    return render(request, "post_app/create_post.html")

