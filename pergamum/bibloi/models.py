from django.urls import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager


class Person(models.Model):
    GROUPS = (
        ('POLIT', _('Politician')),
        ('PERIO', _('Journalist')),
        ('ANALI', _('Analyst')),
    )

    name = models.CharField(_('name'), max_length=100)
    bio = models.TextField(_('bio'), blank=True)
    group = models.CharField(_('group'), max_length=5, choices=GROUPS, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')


class Theme(MPTTModel):
    name = models.CharField(_('name'), max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    order = models.PositiveIntegerField(_('order'))

    class MPTTMeta:
        order_insertion_by = ['order']

    def save(self, *args, **kwargs):
        super(Theme, self).save(*args, **kwargs)
        Theme.objects.rebuild()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Theme')
        verbose_name_plural = _('Themes')


class Source(models.Model):
    name = models.CharField(_('name'), max_length=50, unique=True)
    url = models.URLField(_('url'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')


class Article(models.Model):
    name = models.CharField(_('title'), max_length=1024)
    created_at = models.DateTimeField(_('created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated'), auto_now=True)
    date = models.DateField(_('date'))
    content = models.TextField(_('content'))
    themes = models.ManyToManyField(Theme, blank=True, verbose_name=_('themes'), related_name='articles')

    source = models.ForeignKey(Source, blank=True, null=True)
    url = models.URLField(_('url'), blank=True)
    source_notes = models.TextField(_('Source Notes'), blank=True)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bibloi:detail', args=[str(self.id)])

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')