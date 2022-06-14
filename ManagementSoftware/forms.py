from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    """
        Form per il login

        :params username: L'username dell'user
        :params password: La password dell'user
    """
    username = UsernameField(
        error_messages={'required': 'Campo Obbligatorio'},
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder': "Username",

            }
        )
    )
    password = forms.CharField(
        error_messages={'required': 'Campo Obbligatorio'}, label=_('Password'), strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'autofocus': True, 'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )

    remember_me = forms.BooleanField(required=False)
