import os

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from user.models import *
from multiselectfield import MultiSelectField

# Create your models here.
STATUS_CHOICE = [
    ('In-Progress', 'In-Progress'),
    ('Completed', 'Completed')
]
work_progress_choices = [
    ('0', '0%'),
    ('25', '25%'),
    ('50', '50%'),
    ('75', '75%'),
    ('100', '100%'),
]

def upload_location(instance, filename):
    return "docs/%s/images/%s" % (instance.project_img.title, filename)

def upload_location2(instance, filename):
    return "docs/%s/files/%s" % (instance.project.title, filename)

def upload_location1(instance, filename):
    return "docs/%s/%s" % (instance.title, filename)


a = Employee.objects.all()
co_author_choices = [(i.user.username, i.user.username) for i in a]


class Projects(models.Model):
    Author = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    co_author = MultiSelectField(choices=co_author_choices, null=True, blank=True, max_choices=5)
    title = models.CharField(max_length=100, unique=True)
    abstract = models.TextField(max_length=500)
    project_keywords = models.TextField(max_length=500)
    mentor = models.CharField(max_length=100)
    collabrator = models.CharField(max_length=100, default='null')
    start_date = models.DateTimeField(default=datetime.now())
    completion_date = models.DateField('completion date')
    # images = models.ImageField(upload_to=upload_location1,null='True', blank='True')
    status = models.CharField(max_length=11, choices=STATUS_CHOICE, default='blank')
    work_progress = models.CharField(max_length=4,choices=work_progress_choices,default=1)

    def __str__(self):
        return self.title


class Project_Images(models.Model):
    project_images = models.ImageField(upload_to=upload_location, null='True', blank='True')
    project_img = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.project_img.title

    def delete(self, *args, **kwargs):
        os.remove(self.project_images.path)
        super(Project_Images, self).delete(*args, **kwargs)

class Project_Files(models.Model):
    # cover = models.ImageField(upload_to=upload_location, null='True', blank='True')
    upload_documents = models.FileField(upload_to=upload_location2, null='True', blank='True')
    project = models.ForeignKey(Projects, related_name='files', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.project.title

    def delete(self,*args,**kwargs):
        os.remove(self.upload_documents.path)
        super(Project_Files, self).delete(*args,**kwargs)