from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ..manga.models import Manga

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='comment', blank=True)
    comment = models.TextField()
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)], blank=True, null=True)

    def __str__(self):
        return f'{self.manga.title}'

# class Like(models.Model):
#     user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)
#     comment = models.ForeignKey(Comment, related_name='like', on_delete=models.CASCADE)
#     like = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f'{self.like}'