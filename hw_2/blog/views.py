from django.shortcuts import render, get_object_or_404, redirect
from .models import Article

def get_articles(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def get_article(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/article_detail.html', {'article': article})