"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from ladybugs import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('register/', views.register_page),
    path('login/', auth_views.login, name='login', kwargs={'template_name': 'login.html'}),
    path('logout/', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    path('userpage/', views.user_page, name='userpage'),
    path('userpage/edit_password.html', views.edit_password, name='edit_password'),
    path('userpage/edit_user.html', views.user_edit_view, name='edit_user'),
    path('recipe/', views.full_recipe),
    path('main/', views.main_page)
]
