from django.db import models
from django.utils import timezone

# Create your models here.
class request_info(models.Model):
    firstname=models.CharField(max_length=50)
    middlename=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    qualification=models.CharField(max_length=50)
    salary=models.IntegerField()
    panid=models.CharField(max_length=50)
    request_date=models.DateField(default=timezone.now())

    def __str__(self):
        return self.firstname

class response_info(models.Model):
    req_id=models.IntegerField()
    response=models.CharField()
    request=models.CharField()