from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Facebook
from .serializers import FacebookSerializer#, PasswordSerializer
from .services import (CreateFacebookService, DeleteFacebookService,
                       GetFacebookService, PatchFacebookService)


# Create your views here.


class LoginView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, email=None):
        data = request.data
        serializer = FacebookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            fb_service = CreateFacebookService.execute({"data": request.data})
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)





    def get(self, request, pk=None):
        get_user = GetFacebookService.execute({"pk": pk})
        if pk:
            serializer = FacebookSerializer(get_user)
        else:
            serializer = FacebookSerializer(get_user, many=True)
        return Response(serializer.data)


    def patch(self, request, pk=None):
        update_user = request.data
        serializer = FacebookSerializer(data=update_user, partial=True)
        if serializer.is_valid():
            PatchFacebookService.execute({"update_user": update_user})
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




    # def patch(self, request, pk=None, user_password=None):
    #     update_user = request.data
    #     serializer =   PasswordSerializer(data=update_user, partial=True)
    #     if serializer.is_valid():
    #         PatchFacebookService.execute({"update_user": update_user})
    #
    #         if not user_password.check_password(serializer.data.get('old_password')):
    #             return Response({'old_password': ['Wrong password.']},
    #                             status=status.HTTP_400_BAD_REQUEST)
    #
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)







    def delete(self, request, pk=None):
        DeleteFacebookService.execute({"pk": pk})
        return Response({"message": "Deleted"}, status=200)


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class Send_MailView(APIView):
    def post(self, request):

        email_msg = request.data.get("message")
        email_sub = request.data.get("subject")
        # user_in = Facebook.objects.all()
        send_mail(email_msg, email_sub, from_email=settings.EMAIL_HOST_USER, recipient_list=['to_email'])
        return Response('Mail successfully sent')



