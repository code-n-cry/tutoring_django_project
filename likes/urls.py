from django.urls import path

from likes.views import DislikeView, GetLikesPerArticle, LikeView

app_name = "likes"

urlpatterns = [
    path("like/<int:pk>", LikeView.as_view(), name="like"),
    path("dislike/<int:pk>", DislikeView.as_view(), name="unlike"),
    path("getlikes/<int:pk>", GetLikesPerArticle.as_view(), name="getlikes"),
]
