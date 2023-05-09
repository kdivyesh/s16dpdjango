from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=20)
    dob=models.DateField()
    id_num=models.IntegerField()
