from xml.parsers.expat import model
from django.db import models
from login.models import User

class Book(models.Model):
    title = models.CharField(max_length=36)
    author = models.CharField(max_length=36)
    isb_number = models.CharField(max_length=13)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    is_issued = models.BooleanField(default=False)
    issue_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    returened_date = models.DateField(null=True)
    fine = models.IntegerField(default=0)

#Make some migrations



 