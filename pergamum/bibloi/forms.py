from django.forms import ModelForm, TextInput
from suit.widgets import SuitDateWidget
from suit_redactor.widgets import RedactorWidget


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
