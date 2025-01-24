from operator import index

from django.urls import path, re_path


from .views import IndexView, ArticleDetailView

app_name = "mem"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="detail"),
]
