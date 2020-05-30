from django import forms
from django.contrib.auth.models import User

from app.models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            #'email'
        )



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('countries', )