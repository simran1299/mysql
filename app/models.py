from django.db import models

# Create your models here.

class School(models.Model):
    school_name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)

    def __str__(self):
        return self.school_name


class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.student_name
