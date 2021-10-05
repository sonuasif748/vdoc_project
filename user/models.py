from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os
# Create your models here.

gender_choices=[('male','male'),('female','female'),('others','others')]

# CUSTOM Employee MODEL
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_no = models.BigIntegerField()
    profile_pic = models.ImageField(upload_to='Users/Profile_pictures')
    gender = models.CharField(max_length=6, choices=gender_choices)
    address = models.TextField()
    date_of_join = models.DateTimeField(default=datetime.now())
    remark = models.TextField(max_length=500)
    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        os.remove(self.profile_pic.path)
        super(Employee, self).delete(*args, **kwargs)
