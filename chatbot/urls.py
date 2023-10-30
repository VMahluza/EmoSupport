from django.urls import path
from .views import ChatBotView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from authentication.views import login_redirect_url
from django.conf.urls.static import static


urlpatterns = [
    path('', ChatBotView.as_view(), name='chatbot'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
