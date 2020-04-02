from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    #
    # def clean(self, *args, **kwargs):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #
    #     if User.objects.filter(username=username).exists():
    #         if not password == User.objects.filter(password=password):
    #             raise forms.ValidationError('Wrong password')
    #     return super(LoginForm, self).clean(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('User is not exists')
        return username

