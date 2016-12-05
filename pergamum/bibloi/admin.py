from django.contrib import admin
from django.forms import ModelForm, TextInput
from reversion.admin import VersionAdmin
from suit_redactor.widgets import RedactorWidget
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        widgets = {
            'name': TextInput(attrs={'class': 'input-xxlarge'}),
            'content': RedactorWidget(editor_options={'lang': 'es',
                                                      'minHeight': 400,
                                                      'maxHeight': 800})
        }


@admin.register(Article)
class ArticleAdmin(VersionAdmin):
    form = ArticleForm

