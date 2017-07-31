from django import forms
from .models import Comment, Post
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tinymce.widgets import TinyMCE

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email',max_length=50)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name',max_length=50)
    password1 = forms.CharField(help_text='Please enter a password, must be at least 8 characters',
                                 widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('email','first_name','last_name','password1','password2')

class LoginForm(forms.Form):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Email and Password do not match!")

        return super(LoginForm, self).clean(*args, **kwargs)
    class Meta:
        model = User
        fields = ('username', 'password', )

class PostForm(forms.ModelForm):
    text = forms.CharField(help_text='Enter your Post here', widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    name = forms.CharField(widget=forms.HiddenInput(), initial='User')
    created_on = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now())
    email = forms.CharField(help_text='Not compulsory', required=False)

    class Meta:
        model = Post
        fields = ('author', 'title', 'email', 'text',)

class CommentForm(forms.ModelForm):
    text = forms.CharField(help_text='Enter a Comment',widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    name = forms.CharField(widget=forms.HiddenInput(), initial="User")
    created_on = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now())
    email = forms.CharField(widget=forms.HiddenInput(), initial="default@gmail.com")
    post = forms.CharField(widget=forms.HiddenInput(),initial="Post")

    class Meta:
        model = Comment
        fields = ('text',)
