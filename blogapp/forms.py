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

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            self.add_error('password1', "Hasła nie są takie same")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) <= 4:
            raise forms.ValidationError("Nazwa użtykownika powinna mieć conajmniej 5 znaków")
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("Użytkownik o takim username isnieje.")
        except User.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("Ten email jest już używany przez innego użytkownika")
        except User.DoesNotExist:
            return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) <= 5:
            raise forms.ValidationError("Hasło musi mieć conajmniej 6 znaków")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        # if len(password2) <= 5:
        #     raise forms.ValidationError("Hasło musi mieć conajmniej 6 znaków")
        return password2


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
