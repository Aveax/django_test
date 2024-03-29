from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={'id': self.id})
