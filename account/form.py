from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from account.validator import phone_validator, pass_validator

class SignUpForm(forms.Form):
    email = forms.EmailField(
        label=_('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={'style': 'width:40%;'
                            'border:2px solid rgb(243,134,58);'
                            'outline:none;'
                            'border-radius:7px;'
                            'padding:5px;'
                            'placeholder:something@gmail.com;'
                            'background-color:rgba(253,205,76,0.1)'
                   })
    )
    phone = forms.CharField(
        validators=[phone_validator()],
        label=_('Phone'),
        required=True,
        widget=forms.TextInput(attrs={'style': 'width:40%;'
                                               'border:2px solid rgb(243,134,58);'
                                               'outline:none;'
                                               'border-radius:7px;'
                                               'padding:5px;'
                                               'placeholder:+989132556465;'
                                               'background-color:rgba(253,205,76,0.1)'})
    )
    password = forms.CharField(
        label=_('password'),
        required=True,
        widget=forms.PasswordInput(attrs={'style': 'width:40%;'
                                                   'border:2px solid rgb(243,134,58);'
                                                   'outline:none;'
                                                   'border-radius:7px;'
                                                   'padding:5px;'
                                                   'placeholder:KianoushNasr1378;'
                                                   'background-color:rgba(248,177,67,0.1)'})
    )
    password2 = forms.CharField(
        label=_('confirm password'),
        required=True,
        widget=forms.PasswordInput(attrs={'style': 'width:40%;'
                                                   'border:2px solid rgb(243,134,58);'
                                                   'outline:none;'
                                                   'border-radius:7px;'
                                                   'padding:5px;'
                                                    'background-color:rgba(248,177,67,0.1)'
                                          })
    )

    def clean(self):
        password = self.cleaned_data.get('password')
        repeated_password = self.cleaned_data.get('password2')
        if password == repeated_password:
            raise ValidationError(_('Your inputed passwords is not compatible to each other'))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not pass_validator(password):
            raise ValidationError(_('Your password must be contained alphanumeric and digit'))
        return password