from django.urls import path

from mem.views import (ArticleCreateView, ArticleDeleteView, ArticleDetailView,
                       ArticleUpdateView, IndexView, MyArticles)

app_name = "mem"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("article/create/", ArticleCreateView.as_view(), name="create"),
    path("article/edit/<int:pk>/", ArticleUpdateView.as_view(), name="edit"),
    path(
        "article/delete/<int:pk>/", ArticleDeleteView.as_view(), name="delete"
    ),
    path("my", MyArticles.as_view(), name="my"),
]
