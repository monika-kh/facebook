# from django.urls import reverse
# from django.contrib.auth.models import AbstractUser
from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate
from rest_framework.permissions import IsAuthenticated

from .. import views
from ..models import Facebook
# from login_logout.serializers import FacebookSerializer

# from ..views import LoginView


class LoginTest(APITestCase):
    def setUp(self):
        request = APIClient()
        self.user = Facebook.objects.create_user(username='test', password='test123')
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def test_token_auth(self):
        res = self.client.login(username='test', password='test123')
        self.assertTrue(res)
        breakpoint()


