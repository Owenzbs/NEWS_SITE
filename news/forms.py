from .models import News
from django import forms

class NewsForm(forms.Form):
    title= forms.CharField(max_length=150)
    link= forms.CharField(max_length=300)
    author_name= forms.CharField(max_length=150)
    
    
class CommentsForm(forms.Form):
    author_name= forms.CharField(max_length=150)
    content=forms.CharField(max_length=250)
  
