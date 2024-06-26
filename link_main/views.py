from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters
from authentication.models import User
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q  # For combining queries with OR
from  .serializers import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class GetLinksView(APIView):
    def post(self, request):
        post_data = request.data
        user_id = post_data.get('id')

        if not user_id:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            links_objects = LinkModel.objects.filter(user=user)
            if not links_objects.exists():
                return Response({'error': 'No link found for the user'}, status=status.HTTP_404_NOT_FOUND)

            serializer = LinkSerializer(links_objects, many=True)
            res_data = serializer.data
            return Response(res_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class CreateUpdateLinkView(APIView):
    def post(self, request):
        serializer = LinkSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "Link Posted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        try:
            messege_id = request.data.get('id')
            messege = LinkModel.objects.get(id=messege_id)
        except LinkModel.DoesNotExist:
            return Response("Limk not found", status=status.HTTP_404_NOT_FOUND)

        serializer = LinkSerializer(messege, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Limk updated successfully", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


