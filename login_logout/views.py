from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Facebook
from .serializers import FacebookSerializer
from .services import (CreateFacebookService, GetFacebookService, PatchFacebookService, DeleteFacebookService)


# Create your views here.



class LoginView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        data = request.data
        serializer = FacebookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            fb_service = CreateFacebookService.execute({'data': request.data})
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def get(self, request, pk=None):
        get_user = GetFacebookService.execute({'pk': pk})
        if pk:
            serializer = FacebookSerializer(get_user)
        else:
            serializer = FacebookSerializer(get_user, many=True)
        return Response(serializer.data)

    def patch(self, request, pk=None):
        update_user = request.data
        serializer = FacebookSerializer(data=update_user, partial=True)
        if serializer.is_valid():
            PatchFacebookService.execute({'update_user': update_user})
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status= 400)

    def delete(self, request, pk=None):
        DeleteFacebookService.execute({'pk':pk})
        return Response({'message':'Deleted'}, status=200)
