# appointments/urls.py
from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('book/<int:doctor_pk>/', views.book_appointment, name='book'),
    path('cancel/<int:pk>/', views.cancel_appointment, name='cancel'),
]