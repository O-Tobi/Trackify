from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('register', views.register, name='register'),
    path('register', views.register, name='register'),
    path('login_view', views.login_view, name='login'),
    path('logout_view', views.logout, name='logout')
    
]