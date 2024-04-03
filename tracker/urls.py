from django.urls import path 
from .views import CreateCompanyAPI, ShowCompanyAPI

urlpatterns = [
  path('create/', CreateCompanyAPI.as_view(), name='create-company'),
  path('show/', ShowCompanyAPI.as_view(), name='show-company')

]