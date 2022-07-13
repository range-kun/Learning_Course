from django import forms
from .models import Post, Category


class NewsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_content'].widget = forms.Textarea(attrs={'class': 'form-control',
                                                                   'placeholder': 'Текст записи',
                                                                   'rows': 4})
        self.fields['category'].widget.attrs = {'class': 'custom-select'}
        self.fields['author'].widget.attrs = {'class': 'form-control'}
        self.fields['type_of_content'].widget.attrs = {'class': 'custom-select'}
        self.fields['header'].widget.attrs = {'class': 'form-control', 'placeholder': 'Загаловок'}

    class Meta:
        model = Post
        fields = ['author', 'header', 'type_of_content', 'category', 'text_content']
        labels = {'text_content': '', 'author': 'Автор', 'category': 'Категория', 'header': '',
                  'type_of_content': 'Тип записи'}


class PostChangeListFrom(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),
                                              required=False)
