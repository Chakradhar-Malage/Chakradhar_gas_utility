"""
URL configuration for gas_utility project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import *
from django.contrib import admin
from django.urls import path, include
from company_portal import views as company
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", include("company_portal.urls")),
    path("Chiku", company.Chiku, name="Chiku"),
    # path("abc",company.index,name='index'),
    path("login_page/",company.user_login,name='login'),
    path("reg",company.reg,name='reg'),
    path("request_services", company.request_services,name='request_services'),
    path('submit_request', company.submit_request, name='submit_request'),
    path('logged_in/', company.logged_in, name='logged_in'),
    path('login_emp_page', company.login_emp_page, name="login_emp_page"),
    path('track_requests/', company.track_requests,name='track_requests'),
    path('logout/', auth_views.LogoutView.as_view(next_page='homepage'), name="logout"),
  # Redirect after logout

]

