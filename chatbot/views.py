from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class ChatBotView(LoginRequiredMixin, TemplateView):
    template_name = 'chatbot.html'
    success_url = '/scanning'
    login_url = '/auth/login/'

