from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.Register_Form, name= 'register'),
    path('login/', views.login_form, name= 'login'),
    path('profile/', views.profile_view, name= 'profile'),
]