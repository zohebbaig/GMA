from django import forms
from messaging.models import Message, UserProfile, Group
from django.contrib.auth.models import User


class MessageForm(forms.ModelForm):
    text = forms.CharField(max_length=256, help_text="Please enter a message")

    class Meta:
        model = Message
        fields = ('text',)


class GroupForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter a name for your group.", widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=1024, help_text="Please enter your description.", widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Group
        fields = ('name', 'description')


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(help_text="Please enter your first name.",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(help_text="Please enter your last name.",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(help_text="Please enter your email address.",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(help_text="Please enter a password.",
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(help_text="Please enter your first name.",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(help_text="Please enter your last name.",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(help_text="Please enter your email address.",
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserProfileForm(forms.ModelForm):
    introduction = forms.CharField(max_length=1024, help_text="Please introduce yourself.", widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('introduction',)