from django.shortcuts import render

# Create your views here.
def render_registration(request):
    if request.method == "POST":
        print(request.POST)
    return render(request= request, template_name= 'user_app/registration.html')