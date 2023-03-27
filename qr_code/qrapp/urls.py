from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('qr_code/', views.qr_code_view, name='qr_code_view'),
]
