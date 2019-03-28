from django import forms
from .models import (
    FacebookPageID,
    FacebookAccessToken,
)


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class FacebookPageIDAddForm(forms.ModelForm):

    class Meta:
        model = FacebookPageID
        fields = ['name', 'page_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })


class FacebookAccessTokenAddForm(forms.ModelForm):

    class Meta:
        model = FacebookAccessToken
        fields = ['token']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })
