from allauth.account.forms import SignupForm, LoginForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UpdateUserForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'Email'}
        self.fields['username'].widget.attrs = {'class': 'form-control', 'placeholder': 'Username'}
        self.fields['race'].widget.attrs = {'class': 'form-select', 'placeholder': 'Раса персонажа'}

    class Meta:
        model = User
        fields = ('username', 'email', 'race')


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        my_fields = {'login': 'Логин', 'password': 'Пароль'}
        for field, label in my_fields.items():
            self.fields[field].widget.attrs = {'class': 'form-control margx2'}
            self.fields[field].label = label


class MySignUpForm(SignupForm):
    HUMAN = 'HUM'
    ORC = 'ORC'
    UNDEAD = 'UND'
    NIGHT_ELVES = 'NIE'
    RACES = [(HUMAN, 'Человек'), (ORC, 'Орк'),
             (UNDEAD, 'Нежеть'), (NIGHT_ELVES, 'Ночные эльфы')]

    race = forms.ChoiceField(choices=RACES)

    def __init__(self, *args, **kwargs):
        super(MySignUpForm, self).__init__(*args, **kwargs)
        my_fields = {'email': 'Email', 'password1': 'Пароль', 'password2': 'Пароль еще раз'}
        for field, placeholder in my_fields.items():
            self.fields[field].widget.attrs = {'class': 'form-control marg', 'placeholder': placeholder}
            self.fields[field].label = ''
        self.fields['race'].widget.attrs = {'class': 'form-select marg',}
        self.fields['race'].label = 'Раса персонажа'

    def save(self, request):
        user = super(MySignUpForm, self).save(request)
        user.race = self.cleaned_data['race']
        user.save()
        return user

