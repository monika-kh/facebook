import unittest

import factory
from django.contrib.auth.models import User
from django.test import TestCase
from login_logout.models import Facebook
from .factories import FacebookFactory


class FacebookModelTest(unittest.TestCase):
    def test_fb_factory(self):
        facebook = FacebookFactory(
            first_name='shivam',
            last_name='singh',
            username='shivam',
            email='shivam@asd.com',
            name='shivam',
            language='hindi',
            hometown='bhopal',
            gender='male',
            birthdate='1991-08-11',
            location='indore'
        )

        self.assertEqual(facebook.first_name, 'shivam')
        self.assertEqual(facebook.last_name, 'singh')
        self.assertEqual(facebook.username, 'shivam')
        self.assertEqual(facebook.email, 'shivam@asd.com')
        self.assertEqual(facebook.name, 'shivam')
        self.assertEqual(facebook.language, 'hindi')
        self.assertEqual(facebook.hometown, 'bhopal')
        self.assertEqual(facebook.gender, 'male')
        self.assertEqual(facebook.birthdate, '1991-08-11')
        self.assertEqual(facebook.location, 'indore')

