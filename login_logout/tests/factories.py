import datetime

import factory
import factory.fuzzy
from django.contrib.auth.models import User
from login_logout.models import Facebook


class FacebookFactory(factory.Factory):
    class Meta:
        model = Facebook

    first_name = factory.fuzzy.FuzzyText(length=50)
    last_name = factory.fuzzy.FuzzyText(length=50)
    username = factory.fuzzy.FuzzyText(length=50)
    email = factory.fuzzy.FuzzyText(length=50)
    name = factory.fuzzy.FuzzyText(length=50)
    language = factory.fuzzy.FuzzyText(length=50)
    hometown = factory.fuzzy.FuzzyText(length=50)
    gender = factory.fuzzy.FuzzyText(length=50)
    birthdate = factory.fuzzy.FuzzyDate(datetime.date(1900, 1, 1))
    location = factory.fuzzy.FuzzyText(length=50)

    # first_name = factory.Sequence(lambda n: 'first_name_{}'.format(n))
    # last_name = factory.Sequence(lambda n: 'last_name_{}'.format(n))
    # username = factory.Sequence(lambda n: 'username_{}'.format(n))
    # email = factory.LazyAttribute(lambda o: '@example.com' + o.first_name)
    # name = factory.Sequence(lambda n: 'name_{}'.format(n))
    # language = factory.Sequence(lambda n: 'language_{}'.format(n))
    # hometown = factory.Sequence(lambda n: 'hometown_{}'.format(n))
    # gender = factory.Sequence(lambda n: 'gender_{}'.format(n))
    # birthdate = factory.fuzzy.FuzzyDate(datetime.date(1900, 1, 1))
    # location = factory.Sequence(lambda n: 'location_{}'.format(n))




