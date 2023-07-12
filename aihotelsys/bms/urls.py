from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('calendar/', views.calendar, name='calendar'),
     path('client/', views.client, name='client'),
      path('booking/', views.booking, name='booking'),
      path('finance/', views.finance, name='finance'),
      path('login/', views.login_view, name='login'),
    path('accounts/login/', views.login_view, name='login'),
      path('logout/', views.logout_view, name='logout_view'),
    # Add more URL patterns for your app's views
]
