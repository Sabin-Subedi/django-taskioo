from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def login(request):
    return render(request,'login.html')

def forgot_password(request):
    return render(request,'forgot_password.html')

def signup(request):
    return render(request,'signup.html')

def dashboard(request):
    return HttpResponseRedirect(redirect_to="/login")