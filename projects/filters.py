import django_filters
from django import forms
from .models import *
from user.models import *
from django.contrib.auth.models import User

class ListFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    project_keywords = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model : Projects
        fields = ['title','project_keywords','Author']

class Filterss(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    project_keywords = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Projects
        fields = ['title','project_keywords','Author']

class Userlist(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['id','phone_no','date_of_join']