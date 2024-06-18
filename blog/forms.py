# from .models import Comment
# from django import forms
from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your post content here',
        })

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']