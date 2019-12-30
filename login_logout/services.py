from service_objects.services import Service

from . models import Facebook



class CreateFacebookService(Service):
    def process(self):
        user = Facebook.objects.create(first_name=self.data.get('data').get('first_name'),
                                       last_name=self.data.get('data').get('last_name'),
                                       email=self.data.get('data').get('email'),
                                       name=self.data.get('data').get('name'),
                                       language=self.data.get('data').get('language'),
                                       gender=self.data.get('data').get('gender'),
                                       dob=self.data.get('data').get('dob'),
                                       location=self.data.get('data').get('location'),
                                       username=self.data.get('data').get('username')
        )

        return user



