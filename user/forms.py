from django import forms
from django.contrib.auth.models import User
from .models import *


class Employee_user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name"]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control '}),
            'email': forms.EmailInput(attrs={'class': 'form-control '}),
            # 'password': forms.PasswordInput(attrs={'class': 'form-control '}),
            'first_name': forms.TextInput(attrs={'class': 'form-control '}),
            'last_name': forms.TextInput(attrs={'class': 'form-control '}),
        }


class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["phone_no","profile_pic","gender","address","remark"]

        gender_choices = [('male', 'male'), ('female', 'female'), ('others', 'others')]

        widgets = {
            'phone_no': forms.NumberInput(attrs={'class': 'form-control '}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control '}),
            'gender': forms.Select(attrs={'class': 'form-control '}, choices=gender_choices),
            'address': forms.TextInput(attrs={'class': 'form-control '}),
            'remark': forms.TextInput(attrs={'class': 'form-control '}),
        }

class Status_form(forms.ModelForm):
    class Meta:
        fields = ['status']