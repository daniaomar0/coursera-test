from django import forms
from .models import InstructorModel,InstructorProfile
from apps.signing.models import CustomUser

class loginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=8,widget=forms.PasswordInput)
    
class InstructorSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)  

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create a profile and mark the user as an instructor
            InstructorProfile.objects.create(user=user, is_instructor=True)
        return user

class InstructorForm(forms.ModelForm):
    
    class Meta:
        model = InstructorModel
        fields = '__all__'


        

