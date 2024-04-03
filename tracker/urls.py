from django.urls import path 
from . import views

urlpatterns = [
  path('create_company/', views.CreateCompanyAPI.as_view(), name='create-company'),
  path('show_company/', views.ShowCompanyAPI.as_view(), name='show-company'),
  path('create_employee/', views.CreateEmployeeAPI.as_view(), name='create-employee'),
  path('show_employee/', views.ShowEmployeeAPI.as_view(), name='show-employee'),
  path('create_device/', views.CreateDeviceAPI.as_view(), name='create-device'),
  path('show_device/', views.ShowDeviceAPI.as_view(), name='show-device'),
  path('create_transaction/', views.CreateTransactionAPI .as_view(), name='create-transaction'),
  path('show_transaction/', views.ShowTransactionAPI.as_view(), name='show-transaction'),
]