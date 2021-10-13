from django.db import models

# print("here you will get : ")
# Create your models here.
# class Question(models.Model):
#     question_text = models.CharField(max_length = 200)
#     pub_date = models.DateTimeField('date published')

# class Choice(models.Model):
#     question = models.ForeignKey(Question,  on_delete= models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


class Contact(models.Model):
    name = models.CharField(max_length=122)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
#     email = models.CharField(max_length=122)
    # desc = models.TextField()
    # date = models.DateField()

