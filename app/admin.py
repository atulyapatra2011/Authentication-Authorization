from django.contrib import admin
from .models import Student


# Register your models here.
class Student_Admin(admin.ModelAdmin):
    list_display = ['stu_id','stu_name','stu_college']
admin.site.register(Student,Student_Admin)

