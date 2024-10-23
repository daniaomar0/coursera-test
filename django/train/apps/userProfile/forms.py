from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField() 
    last_name = forms.CharField()  
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

