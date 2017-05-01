from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    """Registers a new user"""
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control'
                                                          }))    
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput(attrs={
                                                        'class': 'form-control'
                                                           }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


    def clean_password2(self):
        """Validates user passwords"""
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    """Modifies user object"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


class ProfileEditForm(forms.ModelForm):
    """Modifies user's profile"""
    class Meta:
        model = Profile
        fields = ('date_of_birth',)
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'})
        }


