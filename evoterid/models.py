from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
class User(models.Model):
    state=models.CharField(max_length=30,blank=False)
    district=models.CharField(max_length=30,blank=False)
    assembly=models.CharField(max_length=30,blank=False)
    name=models.CharField(max_length=30,blank=False)
    srname=models.CharField(max_length=30,blank=False)
    r_name=models.CharField(max_length=30,blank=False)
    r_srname=models.CharField(max_length=30,blank=False)
    relation=models.CharField(max_length=30,blank=False)
    birthday=models.DateField(blank=False)
    gender=models.CharField(max_length=30,blank=False)
    houseno=models.CharField(max_length=30)
    address=models.CharField(max_length=300,blank=False)
    town=models.CharField(max_length=30,blank=False)
    pin=models.CharField(max_length=30,blank=False)
    email_id=models.CharField(max_length=30,blank=False)
    mo_number=models.CharField(max_length=30,blank=False)
    photo = models.FileField()
    age_p = models.FileField()
    typeageproof=models.CharField(max_length=30,blank=False)
    add_p = models.FileField()
    typeaddproof=models.CharField(max_length=30,blank=False)
    place=models.CharField(max_length=30,blank=False)
    status=models.CharField(max_length=30,default="Nope")

class modification(models.Model):
    state=models.CharField(max_length=30,blank=False)
    district=models.CharField(max_length=30,blank=False)
    assembly=models.CharField(max_length=30,blank=False)
    oldname=models.CharField(max_length=30,blank=False)
    oldsrname=models.CharField(max_length=30,blank=False)
    voterid=models.CharField(max_length=30,blank=False)
    name=models.CharField(max_length=30,blank=False)
    srname=models.CharField(max_length=30,blank=False)
    r_name=models.CharField(max_length=30,blank=False)
    r_srname=models.CharField(max_length=30,blank=False)
    relation=models.CharField(max_length=30,blank=False)
    birthday=models.DateField(blank=False)
    gender=models.CharField(max_length=30,blank=False)
    houseno=models.CharField(max_length=30)
    address=models.CharField(max_length=300,blank=False)
    town=models.CharField(max_length=30,blank=False)
    pin=models.CharField(max_length=30,blank=False)
    email_id=models.CharField(max_length=30,blank=False)
    mo_number=models.CharField(max_length=30,blank=False)

    photo = models.FileField()

    age_p = models.FileField()
    typeageproof=models.CharField(max_length=30,blank=False)

    add_p = models.FileField()
    typeaddproof=models.CharField(max_length=30,blank=False)
    place=models.CharField(max_length=30,blank=False)

class Suggestion(models.Model):
    name=models.CharField(max_length=30,blank=False)
    suggestion=models.CharField(max_length=500,blank=False)
