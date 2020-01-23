# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework.authtoken.models import Token
# from rest_framework.test import force_authenticate
#
# from .. models import Facebook
# from login_logout.serializers import FacebookSerializer
#
#
# class LoginTest(APITestCase):
#     def setUp(self):
#         self.user = Facebook.objects.create_user(
#             username='user@foo.com', email='user@foo.com', password='top_secret')
#         breakpoint()
#         self.token = Token.objects.create(user=self.user)
#         self.token.save()
