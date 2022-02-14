from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Facility(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='facilities')
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    photo_url = models.TextField(max_length=200)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    parking_info = models.TextField(max_length=300)
    acc_entrance = models.BooleanField(max_length=5)
    acc_restroom = models.BooleanField(max_length=5)
    open_now = models.BooleanField(max_length=5)

    def __str__(self):
        return self.name


class Location(models.Model):
    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, related_name='locations')
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.city
