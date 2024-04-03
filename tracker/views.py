from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Company 
from .serializers import CompanySerializer


class CreateCompanyAPI(APIView):
  def post(self, request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




  
