"""
URL configuration for KOPPEE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.reservation, name='reservation'),
    path('delete_reservation/<str:pk>/', views.delete_reservation, name='delete-reservation'),
    path('success_page/<str:pk>/', views.success_page, name='success-page'),
    path('admin_login/', views.admin_login, name='admin-login'),
    path('admin_logout/', views.admin_logout, name='admin-logout'),
    path('admin_panel/', views.admin_panel, name='admin-panel')
]
