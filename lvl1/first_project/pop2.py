""" This script populates the User model of sectiontwo of udemy-django. """
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# fake populate script
import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

# topics = ['Search,' 'Social', 'Marketplace', 'News', 'Games']

# def add_user():
#     ## select index 0 of get_or_create topic to get reference to model instance
#     t = User.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t


def populate(N=5):

    for _ in range(N):
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()
        # print(fake_email)

        entry = User.objects.get_or_create(first=fake_first, last=fake_last, email=fake_email)[0]


if __name__ == "__main__":
    print('populating database')
    populate(20)
    print('populating complete')    