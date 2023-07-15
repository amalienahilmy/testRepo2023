from django.urls import path
from . import views
from bms.views import *

urlpatterns = [
    path('', views.home, name='home'),
     path('calendar/', views.calendar, name='calendar'),
     path('client/', views.client, name='client'),
      path('booking/', views.booking, name='booking'),
      path('add_booking/', views.add_booking, name='add-booking'),
      path('finance/', views.finance, name='finance'),
      path('login/', views.login_view, name='login'),
      path('accounts/login/', views.login_view, name='login'),
      path('logout/', views.logout_view, name='logout_view'),
      path('get-client/', get_client, name='get_client'),
    # Add more URL patterns for your app's views
]
