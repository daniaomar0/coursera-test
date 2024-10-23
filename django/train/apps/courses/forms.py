from django import forms
from django.core.validators import validate_email
from django.contrib.auth import get_user_model
from .models import Course, Section, Lecture
from django.forms import inlineformset_factory,modelformset_factory


# Form for creating a Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','prerequisites','field','image' ]



class AssociateEmailForm(forms.Form):
    email = forms.EmailField(validators=[validate_email], label="Associate Email")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()

        # Check if the email exists in the database
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email isn't registered.")

        return email


#form for creating a Section in a Course
class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title']
       
 #form for adding a lecture in the section
class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'content_type', 'content', 'video']

SectionFormSet = inlineformset_factory(Course, Section, form=SectionForm, extra=1)        
LectureFormSet = inlineformset_factory(Section, Lecture, form=LectureForm, extra=1)




