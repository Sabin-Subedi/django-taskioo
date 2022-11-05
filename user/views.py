from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.


def forgot_password(request):
    return render(request, 'forgot_password.html')


class signup(CreateView):
    form_class = SignUpForm
    template_name = "login.html"
    http_method_names= ['post','get']
    success_url = "/"
    
    
    def post(self,request,*args,**kwargs):
        form =self.form_class(request.POST)
        if form.is_valid():
            requestParams = request.POST
            user = authenticate(request, email=requestParams.get('email'), password=requestParams.get('email'))
             
            print('userr',user)
            if user is not None:
                login(request,user=user)
        
            return render(request,self.template_name,context={"form":form,"message":"Invalid email or password"})
        return render(request,self.template_name,context={"form":form})
    
 


def dashboard(request):
    return HttpResponseRedirect(redirect_to="/login")


class login_view(CreateView):
    form_class = LoginForm
    template_name = "login.html"
    http_method_names= ['post','get']
    success_url = "/"
    
    
    def post(self,request,*args,**kwargs):
        form =self.form_class(request.POST)
        if form.is_valid():
            requestParams = request.POST
            user = authenticate(request, email=requestParams.get('email'), password=requestParams.get('email'))
             
            print('userr',user)
            if user is not None:
                login(request,user=user)
        
            return render(request,self.template_name,context={"form":form,"message":"Invalid email or password"})
        # print(self.get_context_data(**kwargs))x
             
        return render(request,self.template_name,context={"form":form})
    
 

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
