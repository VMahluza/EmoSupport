from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, FormView
from typing import Any, Dict
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import LoginForm, SignUpForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm

def login_redirect_url(request):
    return redirect('scanning')
    
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = 'login'
    login_url = 'login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class LogoutView(View):
    def get(self, request):
        user = User.objects.get(id=self.request.user.id)
        if user.is_active:
            user.is_online = False
            user.save()

        logout(request)
        # return redirect('/login')
        return redirect('login')
    
