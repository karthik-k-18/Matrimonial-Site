#import models
from .models import User

#import forms

from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        #hide label and instead use placeholder
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }



        
