from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView


from .forms import LoginForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy("login"))

def forgot_password(request):
    return render(request, 'forgot_password.html')


class signup(CreateView):
    form_class = SignUpForm
    template_name = "signup.html"
    http_method_names= ['post','get']
    success_url = reverse_lazy('dashboard')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        
        return super().dispatch(request, *args, **kwargs)
        
    
    
    def post(self,request,*args,**kwargs):
        form =self.form_class(request.POST)
        if form.is_valid():
            requestParams = request.POST
            first_name =requestParams.get('full_name').strip().split(' ')[0]
            last_name = ' '.join(requestParams.get('full_name').strip().split(' ')[1:]).strip()
       
            user = User.objects.create_user(first_name=first_name, last_name=last_name,username=requestParams.get('username'),email=requestParams.get('email'),password=requestParams.get('password'))

            if user is not None:
                login(request,user)
                return redirect(self.success_url)
        
            return render(request,self.template_name,context={"form":form,"message":"Something went wrong."})
        return render(request,self.template_name,context={"form":form})
    
 





class login_view(CreateView):
    form_class = LoginForm
    template_name = "login.html"
    http_method_names= ['post','get']
    success_url = "/"
    
        
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        
        return super().dispatch(request, *args, **kwargs)
    
    
    def post(self,request,*args,**kwargs):
        form =self.form_class(request.POST)
        if form.is_valid():
            requestParams = request.POST
            username = User.objects.filter(email=requestParams.get('email'))
    
            if username.exists():
                user = authenticate(username=username[0].username, password=requestParams.get('password'))
                print(user)

                if user is not None:
                    login(request,user=user)
                    return redirect(self.success_url)
        
            return render(request,self.template_name,context={"form":form,"message":"Invalid email or password"})
        # print(self.get_context_data(**kwargs))x
             
        return render(request,self.template_name,context={"form":form})
    
 

