from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {
            'required': 'ユーザ名は必須です。',
            'max_length': 'ユーザ名は30文字以下で入力してください。'
        }
        self.fields['password1'].min_length = 6
        self.fields['password1'].error_messages = {
            'required': 'パスワードは必須です。'
        }

        self.fields['password2'].error_messages = {
            'password_mismatch': 'パスワードが一致しません。'
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 8:
            raise forms.ValidationError(u'ユーザ名は8文字以上で入力してください。')
        return password1

        user_count = User.objects.get(username = username).count()
        if user_count > 0:
            raise forms.ValidationError(_("This username has already existed."))
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 8:
            raise forms.ValidationError(u'パスワードは8文字以上で入力してください。')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError(u'パスワードが一致しません。')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get("password1"))
        if commit:
            user.save()
        return user

class UserProfileCreateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('nick_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page',)

class ImpressionForm(forms.ModelForm):
    class Meta:
        model = Impression
        fields = ('comment',)

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'