from rest_framework import status,views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer

from authApp.serializers.carritoSerializer import carritoSerializer

class carritoCreativeview(views.APIView):
    def post(self,request,*args,**kwargs):
        serializer = carritoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()