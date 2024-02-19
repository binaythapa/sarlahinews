from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.contrib import messages
from articles.models import Article,Category



# Create your views here.
def welcome(request):
    articles = Article.objects.all()
    category= Category.objects.all()
    return render(request, "articles/home.html",{"articles":articles,"categories":category})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})