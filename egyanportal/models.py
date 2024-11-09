from django.db import models

# Create your models here.
class Login(models.Model):
    userid = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=50)
    status = models.CharField(max_length=70)

class registration(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=(1,1))
    enrollment = models.CharField(max_length=100)
    name = models.CharField(max_length=225)
    fname = models.CharField(max_length=225)
    mname = models.CharField(max_length=225)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    course = models.CharField(max_length=200)
    branch = models.CharField(max_length=500)
    year = models.IntegerField(max_length=20)
    mobile = models.IntegerField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    new_file = models.ImageField(null=True)

class Usm(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    program = models.CharField(max_length=200)
    Branch = models.CharField(max_length=200)
    Year = models.IntegerField()
    subject = models.CharField(max_length=500)
    file_name = models.CharField(max_length=200)
    new_file = models.FileField(upload_to='myimage')

class assignment(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    program = models.CharField(max_length=200)
    Branch = models.CharField(max_length=200)
    Year = models.IntegerField()
    subject = models.CharField(max_length=500)
    file_name = models.CharField(max_length=200)
    new_file = models.FileField(upload_to='myimage')

class lecture(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    program = models.CharField(max_length=200)
    Branch = models.CharField(max_length=200)
    Year = models.IntegerField()
    subject = models.CharField(max_length=500)
    file_name = models.CharField(max_length=200)
    link = models.CharField(max_length=100)

class Complaints(models.Model):
    name = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    branch = models.CharField(max_length=300)
    contactno = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=300)
    comp = models.CharField(max_length=1000)
    status = models.CharField(max_length=50)
    reqdate = models.DateTimeField()

class Feedbacks(models.Model):
    name = models.CharField(max_length=200)
    program = models.CharField(max_length=200)
    branch = models.CharField(max_length=300)
    contactno = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=300)
    feed = models.CharField(max_length=1000)
    status = models.CharField(max_length=50)
    reqdate = models.DateTimeField()

class Enquiry(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    contactno = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    enq = models.CharField(max_length=1000)
    enqdate = models.DateTimeField()


class noti(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    notm = models.CharField(max_length=200)
    notdate = models.CharField(max_length=15)

class Adbranch(models.Model):
    id=models.IntegerField(primary_key=True ,auto_created=True)
    branch=models.CharField(max_length=40)
    adddate=models.DateField()

class program(models.Model):
    id=models.IntegerField(primary_key=True,auto_created=True)
    course=models.CharField(max_length=200)
    addate=models.DateField()