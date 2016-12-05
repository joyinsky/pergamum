from django.urls import reverse
from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bibloi:detail', args=[str(self.id)])
