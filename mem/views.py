from django.shortcuts import render, get_object_or_404
from .models import Article


def my_view(request):
    posts = Article.objects.all()
    return render(request, "mem/index.html", {"posts": posts})


def home(request):
    articles = Article.objects.all()
    return render(request, "mem/home.html", {"articles": articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "mem/article_detail.html", {"article": article})
