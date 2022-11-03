from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.


def forgot_password(request):
    return render(request, 'forgot_password.html')


def signup(request):
    form = LoginForm()
    print(form.fields.get('password').widget.attrs)
    return render(request, 'login.html')


def dashboard(request):
    return HttpResponseRedirect(redirect_to="/login")


class login(CreateView):
    form_class = LoginForm
    template_name = "login.html"
    http_method_names= ['post','get']
    
    def get(self,request,*args,**kwargs):
        print(request)
        return super().post(request, *args, **kwargs)
    
    def post(self,request,*args,**kwargs):
        print(request)
        return super().post(request, *args, **kwargs)


# def login(request):
#     form =LoginForm()
#     context = {
#         "form": form
#     }
    
#     if request.method == "POST":
#         form = LoginForm(request.POST)
        
        
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(request, email=data.get('email'), password=data.get('email'))
            

#             if user is not None:
#                 login(request, user)
#                 return redirect("home")
#         else:
#             print(context)
#             return render(request, "login.html",{"form":form})
#     return render(request, "login.html",context)
