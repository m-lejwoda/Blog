# from django.core.exceptions import ValidationError
from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Article, Tag
from django import forms


class CreateEditorArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'tags', 'title', 'image', 'content']

    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=CheckboxSelectMultiple
    )

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not len(title) > 3:
            raise forms.ValidationError("Tytuł jest za krótki")
        return title

class CreateBlogArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['tags', 'title', 'image', 'content']

    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=CheckboxSelectMultiple
    )

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not len(title) > 3:
            raise forms.ValidationError("Tytuł jest za krótki")
        return title


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        # fields = ['post', 'author', 'text']

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     print("pierwsze pola")
    #     print(self.fields)
    #     self.post = kwargs.pop('post')
    #     self.article = kwargs.pop('article')
    #     self.text' = kwargs.pop('text')
    #
    #     print(self.fields)
    #     print("args")
    #     print(args)
    #     print(kwargs)


    # def clean(self):
    #     data = self.cleaned_data
        # first_name = data.get('post')
        # last_name = data.get('author')
        # email = data.get('text')
