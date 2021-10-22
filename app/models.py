from django.db import models

# Create your models here.

class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True)
    stu_name = models.CharField(max_length=50)
    stu_college = models.CharField(max_length=50)

    def __str__(self):
        return self.stu_name
