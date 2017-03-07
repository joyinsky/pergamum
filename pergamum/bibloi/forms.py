from django.forms import ModelForm, TextInput, DateField
from suit.widgets import SuitDateWidget
from suit_redactor.widgets import RedactorWidget
from haystack.forms import HighlightedSearchForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        widgets = {
            'name': TextInput(attrs={'class': 'input-xxlarge'}),
            'content': RedactorWidget(editor_options={'lang': 'es',
                                                      'minHeight': 400,
                                                      'maxHeight': 500}),
            'date': SuitDateWidget,
        }


class PersonForm(ModelForm):
    class Meta:
        widgets = {
            'name': TextInput(attrs={'class': 'input-xxlarge'}),
            'bio': RedactorWidget(editor_options={'lang': 'es',
                                                  'minHeight': 400,
                                                  'maxHeight': 500})
        }


class ArticleSearchForm(HighlightedSearchForm):
    # start_date = DateField(required=False)
    # end_date = DateField(required=False)

    models = [Article, ]

    def search(self):
        form = super(ArticleSearchForm, self).search().models(*self.get_models())
        return form

    def get_models(self):
        return self.models
