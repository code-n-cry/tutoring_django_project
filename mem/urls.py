from django.urls import path


from mem.views import IndexView, ArticleDetailView, ArticleCreateView

app_name = "mem"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="detail"),
    path("article/create/", ArticleCreateView.as_view(), name="create")
]
