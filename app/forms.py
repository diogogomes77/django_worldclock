
from django import forms
from django.contrib.auth.models import User

from app.models import Profile, ChosenCountry, Chosen


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


class ChosenForm(forms.ModelForm):

    class Meta:
        model = Chosen
        fields = (
            'profile',
            'timezone',
            'format',
        )
        widgets = {'profile': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(ChosenForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.format is not None:
            new_choices = list()
            for field, format in list(self.fields['format'].choices):
                format = self.instance.time.strftime(format)
                new_choices.append((field, format))
            self.fields['format'].choices = new_choices
            self.fields['format'].widget.choices = new_choices