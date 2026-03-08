from django.shortcuts import render
from .models import Tag, Post
from user_app.models import Profile
from .forms import PostForm, TagForm
from django.contrib.admin.views.decorators import staff_member_required

def render_create_post(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
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
    
@staff_member_required
def render_create_tag(request):
    form = TagForm() 
    if request.method == 'POST':
        form = TagForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
                                     
    return render(
        request=request,
        template_name= "post_app/create_tag.html",
        context={"form": form}
        )