from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import SuperUser


class LoginForm(forms.ModelForm):
    class Meta:
        model = SuperUser
        fields = ('mobile', 'password')
        widgets = {
            'mobile': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Mobile'}),
            'password': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Password'})
        }




class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = SuperUser
        fields = ('mobile',)

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        qs = SuperUser.objects.filter(mobile=mobile)
        if qs.exists():
            raise forms.ValidationError("mobile is taken")
        return mobile

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = SuperUser
        fields = ('mobile',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = SuperUser
        fields = ('mobile', 'password', 'active', 'superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
