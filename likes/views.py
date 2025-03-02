from http import HTTPStatus

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from likes.models import Like
from mem.models import Article


class LikeView(DetailView, LoginRequiredMixin):
    model = Article

    def post(self, request, *args, **kwargs):
        if not Like.objects.filter(
            article=self.get_object(), user=self.request.user
        ).exists():
            like = Like()
            like.article = get_object_or_404(Article, pk=self.kwargs.get("pk"))
            like.user = self.request.user
            like.save()
            return HttpResponse(status=HTTPStatus.OK)
        return HttpResponse(status=HTTPStatus.FORBIDDEN)


class DislikeView(DetailView, LoginRequiredMixin):
    model = Article

    def post(self, request, *args, **kwargs):
        if Like.objects.filter(
            article=self.get_object(), user=self.request.user
        ).exists():
            like = Like.objects.get(
                article=self.kwargs.get("pk"), user=self.request.user
            )
            like.delete()
            return HttpResponse(status=HTTPStatus.OK)
        return HttpResponse(status=HTTPStatus.FORBIDDEN)


class GetLikesPerArticle(DetailView):
    model = Article

    def get(self, request, *args, **kwargs):
        return Like.objects.filter(article=self.kwargs.get("pk")).count()
