from wsgiref.validate import validator
from django.forms import ModelForm
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# 
class LoginForm(ModelForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={ 'placeholder': 'Enter your email ...'}))
    password = forms.CharField(max_length=255, required=True,widget=forms.PasswordInput(attrs={'type':"password",'placeholder': 'Enter your password ...',}))
    
    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Email does not exist")
    #     return email
    
    
    
    class Meta:
        model = User
        fields = ['email', 'password']


class SignUpForm(ModelForm):
    full_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={ 'placeholder': 'Enter your full name ...'}) ,validators=[RegexValidator('^[a-zA-Z]{4,}(?: [a-zA-Z]+){0,2}$','Enter a valid full name.')])
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={ 'placeholder': 'Enter your email ...'}))
    username = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={ 'placeholder': 'Enter your username ...'}))
    password = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={ 'type':'password','placeholder': 'Enter your password ...'}),validators=[RegexValidator('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$','Password must be at least eight characters including at least one number.')])
    confirm_password = forms.CharField(max_length=255,required=True,widget=forms.TextInput(attrs={ 'type':'password','placeholder': 'Enter your password again...'}),)
   
   
    def clean_confirm_password(self):
        if self.data.get('confirm_password') is not self.data.get('password'):
            print('no match')
            raise ValidationError(message="Confirm password does not match")
   

   
    class Meta:
        model = User
        fields = ['full_name','username','email', 'password',]