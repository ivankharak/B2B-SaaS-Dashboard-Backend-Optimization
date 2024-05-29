from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=50)
    city_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class AppUser(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    customer_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    birthday = models.DateField()
    last_updated = models.DateTimeField(auto_now=True)

class CustomerRelationship(models.Model):
    appuser = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    points = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField()
