from django import forms
from django.contrib.auth.models import User

from app.models import Profile, ChosenCountry


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            #'email'
        )


class ChosenCountryForm(forms.ModelForm):

    class Meta:
        model = ChosenCountry
        fields = (
            'profile',
            'country',
            'format',
        )
        widgets = {'profile': forms.HiddenInput()}