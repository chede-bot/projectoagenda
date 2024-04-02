from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.login, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.login, name='dashboard'),
]