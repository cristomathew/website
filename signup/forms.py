from django import forms
from .models import signup


class signupform(forms.ModelForm):

    class Meta:
        model = signup
        fields = [
        'username',
        'age',
        'email'

        ]
class rawsignupform(forms.ModelForm):
    class Meta:
        model = signup
        fields = [
        'password'
        ]
