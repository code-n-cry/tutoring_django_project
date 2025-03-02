from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  TemplateView, UpdateView)

from mem import models


class IndexView(TemplateView):
    template_name = "mem/index.html"

    def get(self, request, *args, **kwargs):
        posts = models.Article.objects.all()
        context = self.get_context_data()
        context.update(posts=posts, **kwargs)
        return self.render_to_response(context)


class MyArticles(LoginRequiredMixin, TemplateView):
    template_name = "mem/my.html"

    def get(self, request, *args, **kwargs):
        posts = models.Article.objects.filter(author=request.user.pk).all()
        context = self.get_context_data()
        context.update(posts=posts, **kwargs)
        return self.render_to_response(context)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "mem/article_update.html"
    success_url = "/my"
    fields = ["title", "content", "image"]
    model = models.Article

    def get(self, request, *args, **kwargs):
        current_post = models.Article.objects.filter(
            id=int(self.request.get_full_path().split('/')[-2])
        ).first()
        if current_post.author.pk == request.user.pk:
            self.object = current_post
            return super().get(request, *args, **kwargs)
        raise PermissionDenied


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    success_url = "/my"
    model = models.Article

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        current_post = models.Article.objects.filter(
            id=int(self.request.get_full_path().split('/')[-2])
        ).first()
        if current_post.author.pk == request.user.pk:
            return super().post(request, *args, **kwargs)
        raise PermissionDenied


class ArticleDetailView(DetailView):
    model = models.Article
    contect_object_name = "article"
    template_name = "mem/article_detail.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    fields = ["title", "content", "image"]
    template_name = "mem/article_create.html"
    success_url = "/my"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)
