from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from login_logout import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/<int:pk>/", views.LoginView.as_view(), name="login"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("send_mail/", views.Send_MailView.as_view(), name="send_mail"),
]
