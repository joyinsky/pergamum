from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from reversion.admin import VersionAdmin
from suit.admin import SortableModelAdmin
from mptt.admin import MPTTModelAdmin
from attachments.admin import AttachmentInlines
from .forms import ArticleForm, PersonForm
from .models import Article, Person, Theme, Source, Folder


@admin.register(Article)
class ArticleAdmin(VersionAdmin):
    form = ArticleForm

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name', 'date', 'content']
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-classification',),
            'fields': ['folder', 'themes', 'tags']}),
        (None, {
            'classes': ('suit-tab', 'suit-tab-sources',),
            'fields': ['source', 'url', 'source_notes']}),
    ]

    suit_form_tabs = (('general', _('General')),
                      ('classification', _('Classification')),
                      ('sources', _('Sources')),
                      )

    list_display = ['name', 'date', 'source']
    # inlines = (AttachmentInlines,)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    form = PersonForm


@admin.register(Theme)
class ThemeAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('name',)


@admin.register(Folder)
class FolderAdmin(MPTTModelAdmin, SortableModelAdmin):
    mptt_level_indent = 20
    list_display = ('name',)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass
