from django.db import models

from mem.models import Article
from user.models import MyUser


class Like(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='likes'
    )
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'article'], name='unique_like'
            ),
        ]
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
