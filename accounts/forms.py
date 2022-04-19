from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile,Neighbourhood


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        help_texts = {
            'username': None,
            'email': None,
        }
        
class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user','location')
        fields = '__all__'
        
class UpdateNeighbourhoodForm(ModelForm):
    
    class Meta:
        model = Neighbourhood
        fields = ['address',]
        
class ProfileUpdateForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']