from django.contrib.auth import get_user_model
from django.db import models
from applications.manga.models import Manga

User = get_user_model()

class Chapter(models.Model):
    title = models.CharField(max_length=50, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chapter', blank=True)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='')
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='chapter')

    def __str__(self):
        return self.title

