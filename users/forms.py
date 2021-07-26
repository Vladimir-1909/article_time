from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserOurRegistraion(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        })
    )

    password1 = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )

    password2 = forms.CharField(
        label=' ',
        required=False,
        label_suffix=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'display: none;'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1']


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        })
    )

    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )



class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы: @/./+/-/_.',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        })
    )
    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['img'].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ['img']
