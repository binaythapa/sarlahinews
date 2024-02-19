from django.forms import ModelForm, Textarea
from .models import *
from django import forms

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author', 'category', 'tags', 'image']
