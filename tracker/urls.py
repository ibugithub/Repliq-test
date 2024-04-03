from django.urls import path 
from .views import CreateCompanyAPI

urlpatterns = [
  path('create/', CreateCompanyAPI.as_view(), name='create-company')

]