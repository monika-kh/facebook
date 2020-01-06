import email

from rest_framework.response import Response
from service_objects.services import Service

from .models import Facebook


class CreateFacebookService(Service):
    def process(self):
        data = self.data
        email=data.get('data').get('email')
        email_exist = Facebook.objects.filter(email=email).exists()
        if email_exist:
            return email
            #return Response("email already taken")
        else:                                                           # create object when email and username not existing
            user = Facebook.objects.create(
            first_name=self.data.get("data").get("first_name"),
            last_name=self.data.get("data").get("last_name"),
            email=self.data.get("data").get("email"),
            name=self.data.get("data").get("name"),
            language=self.data.get("data").get("language"),
            gender=self.data.get("data").get("gender"),
            birthdate=self.data.get("data").get("birthdate"),
            location=self.data.get("data").get("location"),
            username=self.data.get("data").get("username"),
            hometown=self.data.get("data").get("hometown"),
        )
        user.set_password(self.data.get("data").get("password"))
        user.save()

        return user


class GetFacebookService(Service):
    def process(self):
        pk = self.data.get("pk")
        if pk:
            get_user = Facebook.objects.get(id=pk)
        else:
            get_user = Facebook.objects.all()
        return get_user


class PatchFacebookService(Service):
    def process(self):
        pk = self.data.get("update_user").get("id")
        user_username = self.data.get("update_user").get("username")
        user_first_name = self.data.get("update_user").get("first_name")
        user_last_name = self.data.get("update_user").get("last_name")
        user_email = self.data.get("update_user").get("email")
        user_language = self.data.get("update_user").get("language")
        user_location = self.data.get("update_user").get("location")
        user_birthdate = self.data.get("update_user").get("birthdate")

        patch_user = Facebook.objects.get(id=pk)

        patch_user.username = user_username
        patch_user.first_name = user_first_name
        patch_user.last_name = user_last_name
        patch_user.email = user_email
        patch_user.language = user_language
        patch_user.location = user_location
        patch_user.birthdate = user_birthdate

        patch_user.save()
        return patch_user


class DeleteFacebookService(Service):
    def process(self):
        pk = self.data.get("pk")
        delete_user = Facebook.objects.get(id=pk)
        delete_user.delete()
