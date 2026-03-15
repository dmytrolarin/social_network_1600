from django import forms
from django.core.exceptions import ValidationError
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
        widgets = {
            "name": forms.TextInput(attrs={"class": 'name'})
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        
        if not name[0].isalpha():
            raise ValidationError('Ім`я повинно починатися тільки з літери', params={'value': name})
        
        return name
    
    def clean(self):
        is_active = self.cleaned_data.get('is_active')
        icon = self.cleaned_data.get('icon')
        description = self.cleaned_data.get('description')
        
        if is_active and (not icon or not description):
            raise forms.ValidationError(
                'Вкажіть іконку та опис, якщо тег активний'
            )
            
        return self.cleaned_data  
    
        
    