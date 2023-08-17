from django.db import models

# class Address(models.Model):
#     town = models.CharField()
#     state = models.CharField(default="uttar pradesh")
#     country = models.CharField(default="india")
#     pincode = models.IntegerField()



class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    phone_number = models.CharField(max_length=10)
    email_id = models.EmailField()
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    semester = models.IntegerField()
    addmission_year = models.IntegerField()
