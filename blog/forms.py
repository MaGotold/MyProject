from django import forms 
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your name",
            "text": "Your comment"
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # Setting a placeholder for the user_name field
        self.fields['user_name'].widget.attrs.update({'placeholder': 'optional'})