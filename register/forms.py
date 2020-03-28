from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import validate_email
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = [
#             "username", "email", "password1", "password2"
#         ]


class RegistForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(validators=[validate_email])
    password = forms.CharField(required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username