from django import forms
from .models import Notice, Reply


class NoticeForms(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ['header', 'category', 'text_content',]
        labels = {'header': 'Заголовок', 'category': 'Категория'}


class NoticeFullForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,
                                                                    'accept': 'image/*',
                                                                    'class': 'form-control'}), required=False)

    videos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,
                                                                    'accept': 'video/mp4',
                                                                    'class': 'form-control'}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_content'].widget = forms.Textarea(attrs={'class': 'form-control marg',
                                                                    'placeholder': 'Текст объявления',
                                                                    'rows': 4})
        self.fields['category'].widget.attrs = {'class': 'form-control'}
        self.fields['header'].widget.attrs = {'class': 'form-control'}

    class Meta(NoticeForms.Meta):
        fields = NoticeForms.Meta.fields + ['images', 'videos']


class ReplyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = forms.Textarea(attrs={'class': 'form-control marg',
                                                           'rows': 3})
        self.fields['text'].label = 'Текст отклика'

    class Meta:
        model = Reply
        fields = ['text']
