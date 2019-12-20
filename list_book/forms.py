from django import forms
from .models import Books


class Bookform(forms.ModelForm):

    class Meta:
        model = Books
        fields = ('title', 'author', 'date_published',
                  'number_of_pages', 'type_of_book')
        labels = {
            'date_published': 'Date Published (Format : yyyy-mm-dd)',
            'number_of_pages': 'Number of Pages',
            'type_of_book': 'Genres'
        }

    def __init__(self, *args, **kwargs):
        super(Bookform, self).__init__(*args, **kwargs)
        self.fields['type_of_book'].empty_label = 'Select'
        self.fields['date_published'].required = 'Select'
