from django.db import models

class FirstApp(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    test = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
