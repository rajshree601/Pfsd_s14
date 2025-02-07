from django.db import models

# Create your models here.
class Admin(models.Model): #models.Model is compulsory
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)
    #"blank=flase" (name can't be blank) and "unique=true" (name shoukd be unique)
    class Meta:
        db_table = "admin_table"
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=25, blank=False, unique=True)
    phno = models.CharField(max_length=10, blank=False, unique=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)
    class Meta:
        db_table = "register_table"

class Packages(models.Model):
    id = models.AutoField(primary_key=True)
    tourcode = models.CharField(max_length=10, blank=False, unique=True)
    tourname = models.CharField(max_length=30, blank=False)
    tourpackage = models.CharField(max_length=30, blank=False)
    desc = models.CharField(max_length=35, blank=False)
    class Meta:
        db_table = "package_table"
