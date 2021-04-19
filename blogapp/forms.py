from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CommentForm(ModelForm):
    class Meta:
        model= Comment
        fields=['post','author','text']
    def clean(self):
        data = self.cleaned_data
        first_name = data.get('post')
        last_name = data.get('author')
        email = data.get('text')
