from django.urls import path
from django import *
from . import views
from .views import user_login, logged_in
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.home),
    # path("abc/", views.index, name="index"),
    # path('track_requests/', views.track_requests, name='track_requests'),
    # path('support-dashboard/', views.support_dashboard, name='support-dashboard'),
    # ----------------------------------------------------
    path("login_page/", views.user_login, name="login_page"),
    path("reg", views.reg, name="reg"),
    path("", views.Chiku, name="Chiku"),
    path('', views.homepage, name='homepage'),
    path('request_services', views.request_services, name='request_services'),
    path('submit_request/', views.submit_request, name='submit_request'),
    path('logged_in/', logged_in, name='logged_in'),
    path('login_emp_page', views.login_emp_page, name="login_emp_page"),
    path('track_requests/', views.track_requests, name='track_requests'),
    path("logout/", auth_views.LogoutView.as_view(next_page='homepage'), name="logout"),  # Redirect after logout
    
]
