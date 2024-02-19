from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

#article
def article(request):
    if request.method== "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form= ArticleForm()
    return render(request, 'articles/create.html', {'form':form})

def edit_article(request, id):
    article = get_object_or_404(Article, pk=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/create.html', {'form': form})

'''
def edit_article(request, id):
    article_instance = Article.objects.get(pk=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article_instance)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=id)
    else:
        form = ArticleForm(instance=article_instance)
    return render(request, 'create.html', {'form': form})
'''

def article_detail(request, id):
    articles = Article.objects.all()
    article = get_object_or_404(Article, pk=id)
    category= Category.objects.all() 
    view, created = View.objects.get_or_create(article=article)
    view.count += 1   
    view.save()
    return render(request, "articles/article_detail.html", {'article': article, 'view_count': view.count,"categories":category,"articles":articles})

def article_delete(request, id):    
    data = get_object_or_404(Article, pk=id)
    data.delete()
    return redirect("/")

#category
def category(request):
    if request.method== "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= CategoryForm()
    return render(request, 'articles/create.html', {'form':form})

def category_detail(request,id):
    data = get_object_or_404(Category, pk=id)
    return render(request, "articles/article_detail.html", {'data':data})

def category_delete(request, id):    
    data = get_object_or_404(Category, pk=id)
    data.delete()
    return redirect("/")

#Tag
def tag(request):
    if request.method== "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form= TagForm()
    return render(request, 'articles/create.html', {'form':form})

def tag_detail(request,id):
    data = get_object_or_404(Tag, pk=id)
    return render(request, "articles/article_detail.html", {'data':data})

def tag_delete(request, id):    
    data = get_object_or_404(Tag, pk=id)
    data.delete()
    return redirect("/")




