from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Article


class IndexView(TemplateView):
    template_name = "mem/index.html"

    def get(self, request, *args, **kwargs):
        posts = Article.objects.all()
        context = self.get_context_data()
        context.update(posts=posts, **kwargs)
        return self.render_to_response(context)


def home(request):
    articles = Article.objects.all()
    return render(request, "mem/home.html", {"articles": articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "mem/article_detail.html", {"article": article})
