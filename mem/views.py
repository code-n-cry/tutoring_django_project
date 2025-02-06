from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    fields = ["title", "content"]
    template_name = "mem/article_create.html"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)
