from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView

from mem import models


class IndexView(TemplateView):
    template_name = "mem/index.html"

    def get(self, request, *args, **kwargs):
        posts = models.Article.objects.all()
        context = self.get_context_data()
        context.update(posts=posts, **kwargs)
        return self.render_to_response(context)


class ArticleDetailView(DetailView):
    model = models.Article
    contect_object_name = "article"
    template_name = "mem/article_detail.html"


class ArticleCreateView:
    pass
