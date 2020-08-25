from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url',
                  'facebook_url', 'twitter_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            # 'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        # declare fields to use, username, password1, password2 already in use
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    # this is the way to do it with auth forms
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(
        max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(
        max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(
        max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(
        max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        # This is the order they show up in the form
        # declare fields to use, username, password1, password2 already in use
        fields = ('username', 'first_name', 'last_name',
                  'email', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(
        max_length=255, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'password1', 'password2')
