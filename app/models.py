from django.db import models

# Create your models here.
class Course(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=64)
    faculty=models.CharField(max_length=64)
    class_date=models.DateField(default=True)
    class_time=models.CharField(max_length=54)
    fees=models.FloatField(max_length=34)
    duration=models.IntegerField()

