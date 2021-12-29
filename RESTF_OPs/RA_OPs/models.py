from typing import AsyncContextManager
from django.db import models


class Crudp(models.Model):
    Name=models.CharField(max_length=20, primary_key=True)
    Surname=models.CharField(max_length=20)
    Age=models.IntegerField()
    Hometown=models.CharField(max_length=30)
    Occupation=models.CharField(max_length=50)

    class Meta:
        db_table="crudp"

    def __str__(self):
        return self.Name

class job(models.Model):
    Company_name=models.CharField(max_length=30)
    emp_id=models.IntegerField(max_length=10, primary_key=True)
    emp_name=models.CharField(max_length=30)
    work=models.CharField(max_length=50)

    class Meta:
        db_table="job"

    def __str__(self):
        return self.Company_name

class address(models.Model):
    city=models.CharField(max_length=30)
    pincode=models.IntegerField(max_length=10, primary_key=True)
    district=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    work=models.CharField(max_length=50, default="null")

    class Meta:
        db_table="address"

    def __str__(self):
        return self.city

class Comp(models.Model):

    city=models.CharField(max_length=30)
    pincode=models.IntegerField(max_length=10, primary_key=True)
    district=models.CharField(max_length=30)
    address=models.CharField(max_length=50)

    class Meta:
        db_table="comp"

    def __str__(self):
        return self.city