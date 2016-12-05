from django.contrib import admin
from reversion.admin import VersionAdmin
from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin
from .forms import ArticleForm, PersonForm
from .models import Article, Person, Theme


@admin.register(Article)
class ArticleAdmin(VersionAdmin):
    form = ArticleForm


@admin.register(Person)
class ArticleAdmin(VersionAdmin):
    form = PersonForm


@admin.register(Theme)
class ThemeAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('name',)
