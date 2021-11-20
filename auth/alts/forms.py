from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _


class CustomAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    '''
        Default registration form
    '''
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class EmployeeSignUpForm(UserCreationForm):
    '''
        Customer only registration form
    '''
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.employee = True
        if commit:
            user.save()
        return user


class CustomerSignUpForm(UserCreationForm):
    '''
        Customer only registration form
    '''
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.buyer = True
        if commit:
            user.save()
        return user


class AdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = "__all__"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        return self.initial["password"]


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)


class SetPasswordForm(forms.Form):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    new_password1 = forms.CharField(
        label="New password", widget=forms.PasswordInput)
    new_password2 = forms.CharField(
        label="New password confirmation", widget=forms.PasswordInput)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2
