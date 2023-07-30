from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Users
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    date_of_birth = forms.DateField(required=False)
    mobile = forms.IntegerField(required=False)
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.PasswordInput()

    class Meta:
        model = Users
        fields = ["username", "password"]