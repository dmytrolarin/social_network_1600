from django.shortcuts import render
from .models import Tag, Post
from user_app.models import Profile
from .forms import PostForm


def render_create_post(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        chosen_tags = request.POST.getlist('tags')
        author = Profile.objects.get(user = request.user)
        
        new_post = Post.objects.create(
            title = title,
            content = content,
            image = image,
            author = author
        )
        
        if chosen_tags:
            new_post.tags.set(chosen_tags)
            
    
    return render(
        request, 
        "post_app/create_post.html",
        context={
            'tags': tags,
            'form': PostForm()
            }
        )
    

