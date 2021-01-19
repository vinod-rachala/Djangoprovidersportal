from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserExtension(models.Model):
    contact = models.IntegerField(primary_key=True)
    specialisation = models.CharField(max_length=50)
    profile = models.CharField(max_length=100)
    user = models.OneToOneField(User)

class Problem(models.Model):
    problem_desc = models.CharField(max_length=150)
    doctor = models.ManyToManyField(User)

class Consumer(models.Model):
    name = models.CharField(max_length=50)  
    status = models.CharField(max_length=50)  
    contact = models.IntegerField(primary_key=True)
    precription = models.CharField(max_length=150)
    doctor = models.ManyToManyField(User)  
    age = models.IntegerField(max_length=50)  
    date_of_birth = models.DateField()
    date_of_admission = models.DateField()
    dateofdischarge = models.DateField()
    problem = models.ManyToManyField(Problem)
    risk_score = models.CharField(max_length=50)
    enrolled_program = models.CharField(max_length=20)

  

  