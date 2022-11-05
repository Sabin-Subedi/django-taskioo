from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="signup"),
    path("login/", views.login_view.as_view(), name="login"),
    path("signup/", views.signup.as_view(), name="signup"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
]
