from django.db import models
from datetime import datetime


class Contact(models.Model):
    objects = None
    name = models.CharField(max_length=122,null=True,default=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12,null=True,default=True)
    email = models.CharField(max_length=122,null=True,default=True)
    desc = models.TextField(null=True,default=True)
    # date = models.DateTimeField(default=datetime.now())
    date = models.DateField(null=True,default=True)

    def __str__(self):
        return self.name


class Submit(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=13)
    date = models.DateField()

