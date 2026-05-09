from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('appointments/', include('appointments.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('doctors/', include('doctors.urls')),
    path('ai/', include('ai_orientation.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

