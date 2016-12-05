from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    name = models.CharField(_('title'), max_length=1024)
    created_at = models.DateTimeField(_('created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated'), auto_now=True)
    content = models.TextField(_('content'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bibloi:detail', args=[str(self.id)])

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

