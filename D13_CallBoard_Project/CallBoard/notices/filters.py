import django_filters
from django.db.models import Q
from .models import Notice
from django import forms


class NoticeFilter(django_filters.FilterSet):
    custom_field = django_filters.CharFilter(method='multiple_search', label='',
                                             widget=forms.TextInput(attrs={
                                                 'placeholder': 'Поиск по объявлениям',
                                                 'class': 'form-control'
                                             }))

    class Meta:
        model = Notice
        fields = ('custom_field',)

    def multiple_search(self, queryset, name, value):
        return Notice.objects.filter(Q(text_content__icontains=value) | Q(header__icontains=value))
