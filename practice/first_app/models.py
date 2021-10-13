from django.db import models
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=122,null=False)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, default=True,null=True)
    email = models.CharField(max_length=122, default=True, null=True)
    desc = models.TextField(default=True, null=True)
    # date = models.DateTimeField(default=datetime.now())
    date = models.DateField(default=True,null=True)

