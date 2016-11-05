from django import forms
from .models import Post, Comment

#form for posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

#form for comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
