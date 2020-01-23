from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate

from .. models import Facebook
from login_logout.serializers import FacebookSerializer


class LoginTest(APITestCase):
    def setUp(self):
        self.user = Facebook.objects.create_user(
            username='user@foo.com', password='top_secret')
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        breakpoint()

    # def test_token_auth(self):
    #     force_authenticate(request, token=self.token.key)
    #     view = views.EndpointViewSet.as_view({'get': 'list'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, 200)
    #     json_response = json.loads(response.render().content)['results']