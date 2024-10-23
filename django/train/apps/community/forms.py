from django import forms
from .models import Post,Comment


class postForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['content']  # Assuming your Post model has a 'content' field
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': "What's on your mind?"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Write a comment...'}),
        }