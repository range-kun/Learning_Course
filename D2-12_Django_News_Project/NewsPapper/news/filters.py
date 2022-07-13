import django_filters
from .models import Post
from django import forms


class PostFilter(django_filters.FilterSet):
    my_author = django_filters.CharFilter(label='', field_name='author__user__username', lookup_expr='icontains',
                                          widget=forms.TextInput(attrs={
                                              'placeholder': 'Имя автора', 'class': 'form-control',
                                              'style': 'margin-top: 10px; text-align: center'}))
    my_header = django_filters.CharFilter(label='', field_name='header', lookup_expr='icontains',
                                          widget=forms.TextInput(attrs={
                                              'placeholder': 'Название заголовка', 'class': 'form-control',
                                              'style': 'margin-top: 10px; text-align: center'}))
    my_date = django_filters.DateFilter(field_name='date_of_creation', lookup_expr='gt', label='',
                                        widget=forms.DateInput(attrs={
                                            'placeholder': 'Позже даты (ГГГГ-мм-дд)', 'class': 'form-control',
                                            'style': 'margin-top: 10px; text-align: center; margin-bottom: 10px'}))

    class Meta:
        model = Post
        fields = {}
