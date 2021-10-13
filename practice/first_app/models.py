from django.db import models
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=122)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    # date = models.DateTimeField(default=datetime.now())
    date = models.DateField()

