from django.db import models

class EmployeeModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_no = models.IntegerField(unique=True)
    salary = models.FloatField()
    photo = models.ImageField(upload_to='employee_images')
    address = models.TextField()
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=60)
