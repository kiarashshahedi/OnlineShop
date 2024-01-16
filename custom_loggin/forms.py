from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class RegisterForm(forms.ModelForm):
    otp = forms.IntegerField()
    class Meta:
        model = MyUser
        fields = ['mobile', 'otp'] 
#---------------------------------------------------------
