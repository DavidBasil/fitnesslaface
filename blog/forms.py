from django import forms
from .models import Comment, Post


class SharePostForm(forms.Form):
    """Lets user share the post vie email"""
    name = forms.CharField(max_length=20, 
                           widget=forms.TextInput(attrs={
                                                  'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                                     'class': 'form-control'
                                                     }))
    to = forms.EmailField(widget=forms.EmailInput(attrs={
                                                  'class': 'form-control'
                                                  }))
    comments = forms.CharField(required=False, widget=forms.Textarea(
                                            attrs={'class': 'form-control'}))


class CommentForm(forms.ModelForm):
    """Lets users comment on a post"""
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    """Lets user create a new post or update an existing one"""
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }



