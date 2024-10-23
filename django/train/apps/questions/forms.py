from django import forms
from .models import Step1,Step2

class Step1Form(forms.ModelForm):
    
    class Meta:
        model = Step1
        fields = '__all__'

class Step2Form(forms.ModelForm):
    
    class Meta:
        model = Step2
        fields = '__all__'
   
