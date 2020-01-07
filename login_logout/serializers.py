from rest_framework import serializers

from . models import Facebook


class FacebookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facebook
        fields = "__all__"
        extra_kwargs = {
           'password': {'default': 'password', "write_only": "True"},
         }

# class PasswordSerializer(serializers.Serializer):
#     """
#     Serializer for password change endpoint.
#     """
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)