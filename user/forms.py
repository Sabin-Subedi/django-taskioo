from django.forms import ModelForm
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class LoginForm(ModelForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={ 'placeholder': 'Enter your email ...'}))
    password = forms.CharField(max_length=255, required=True,widget=forms.PasswordInput(attrs={'type':"password",'placeholder': 'Enter your password ...',}))
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email does not exist")
        return email
    
    
    
    class Meta:
        model = User
        fields = ['email', 'password']
