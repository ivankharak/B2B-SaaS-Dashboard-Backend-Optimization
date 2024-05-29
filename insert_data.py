import os
import django
import random
from faker import Faker
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_again.settings')
django.setup()

from crmApp.models import AppUser, Address, CustomerRelationship

fake = Faker()

def create_address():
    return Address.objects.create(
        street=fake.street_name(),
        street_number=fake.building_number(),
        city_code=fake.postcode(),
        city=fake.city(),
        country=fake.country()
    )

def create_app_user(address):
    return AppUser.objects.create(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        gender=random.choice(['M', 'F', 'O']),
        customer_id=fake.uuid4(),
        phone_number=fake.phone_number(),
        address=address,
        birthday=fake.date_of_birth(minimum_age=18, maximum_age=90),
        last_updated=fake.date_time_this_decade()
    )

def create_customer_relationship(appuser):
    return CustomerRelationship.objects.create(
        appuser=appuser,
        points=random.randint(0, 10000),
        created=appuser.created,
        last_activity=fake.date_time_between(start_date=appuser.created, end_date="now")
    )

def insert_data(n):
    for _ in range(n):
        address = create_address()
        appuser = create_app_user(address)
        create_customer_relationship(appuser)
  
if __name__ == '__main__':
    insert_data(3000000)
