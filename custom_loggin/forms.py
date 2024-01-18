from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['mobile', ]
#---------------------------------------------------------
