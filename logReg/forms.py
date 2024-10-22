from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, password_validation, get_user_model

from .models import CustomUser

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ['name', 'surname', 'email', 'phone']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = f"{self.cleaned_data["name"]}{self.cleaned_data["email"]}"
        if commit:
            user.save()
        return user

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Invalid password!!")
        return password2
    
    def clean_name(self):
        return self.cleaned_data['name']
    
    def clean_surname(self):
        return self.cleaned_data['surname']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = _('Имя')
        self.fields['surename'].widget.attrs['placeholder'] = _('Фамилия')
        self.fields['email'].widget.attrs['placeholder'] = _('Почта')
        self.fields['phone'].widget.attrs['placeholder'] = _('Телефон')
        self.fields['password1'].widget.attrs['placeholder'] = _('Пароль')
        self.fields['password2'].widget.attrs['placeholder'] = _('Подтверждение пароля')
        self.fields['password1'].widget.attrs['id'] = 'password-input'
        self.fields['password2'].widget.attrs['id'] = 'password-input1'
        
User = get_user_model()

class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта', max_length= 254, required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)

        if not user:
            raise forms.ValidationError('Неверная почта или пароль')
        
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = _('Почта')
        self.fields['password'].widget.attrs['placeholder'] = _('Пароль')
        self.fields['password'].widget.attrs['id'] = 'password-input'
