from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.MyUser
        fields = ['mobile', ]
#---------------------------------------------------------
