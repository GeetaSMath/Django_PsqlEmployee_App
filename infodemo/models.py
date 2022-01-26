from django.db import models

# Create your models here.

class employee(models.Model):

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    salary = models.IntegerField()
    status = models.BooleanField()

    # create /insert/ add - GET
    # Retrive /Fetch -GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE
