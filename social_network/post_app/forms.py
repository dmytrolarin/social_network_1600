from django import forms
from .models import Tag


class PostForm(forms.Form):
    title = forms.CharField(max_length= 50, required= True)
    content = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField() 
    tags = forms.ModelMultipleChoiceField(
        queryset= Tag.objects.all(),
    )
    
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'