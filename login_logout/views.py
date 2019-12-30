from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Facebook
from .serializers import FacebookSerializer
from .services import CreateFacebookService


# Create your views here.



class LoginView(APIView):
    def post(self, request):
        data = request.data
        serializer = FacebookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            fb_service = CreateFacebookService.execute({'data': request.data})
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    #
    # def get(self, request):
    #     import pdb;
    #     pdb.set_trace()
