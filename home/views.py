from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, FormView
from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chatname'] = 'Emo'
        return context
    
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chatname'] = 'Emo'
        return context
    
    def get_login_url(self) -> str:
        return "login"

def scanning(request):
    return render(request, 'scanfinger.html', {})