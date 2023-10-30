from django.urls import path
from .views import HomeView, LandingPageView, scanning
from django.contrib import admin
from django.urls import include, path
from authentication.views import login_redirect_url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('home', HomeView.as_view(), name='home'),
    path('scanning', scanning, name='scanning'),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
