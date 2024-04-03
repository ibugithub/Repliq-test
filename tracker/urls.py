from django.urls import path 
from .views import CreateCompanyAPI, ShowCompanyAPI

urlpatterns = [
  path('create_company/', CreateCompanyAPI.as_view(), name='create-company'),
  path('show_company/', ShowCompanyAPI.as_view(), name='show-company'),
]