from django.db import models
from django.contrib.auth.models import User,Group
from lessons.models import *

#TODO:is your field have blank=False and null=False if you add new field to your model past models will get an error in database so sloution is add default option to you model

class AllUsersMetaData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    age = models.PositiveSmallIntegerField(blank=False)
    is_teacher = models.BooleanField(default=False,blank=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class TeachersMetaData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    phone_number = models.PositiveBigIntegerField(blank=False)
    lessons = models.ManyToManyField(Lesson,blank=False)
    classes = models.ManyToManyField(Group,blank=False)
    def __str__(self):
        user_metadata = AllUsersMetaData.objects.filter(user=self.user).first()
        return f"{user_metadata.first_name} {user_metadata.last_name}"

class StudentsMetaData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    address = models.CharField(max_length=300,blank=False)
    father_phone_number = models.PositiveBigIntegerField(blank=False)
    mother_phone_number = models.PositiveBigIntegerField(blank=False)
    home_phone_number = models.PositiveBigIntegerField(blank=False)
    GRADE_CHOICES = [
        ('1', 'دهم'),
        ('2', 'یازدهم '),
        ('3', 'دوازدهم'),        
    ]
    grade = models.CharField(max_length=1,choices=GRADE_CHOICES,blank=False)
    SUBJECT_CHOICES = [
        ('1', 'تجربی'),
        ('2', 'ریاضی'),
        ('3', 'انسانی'),
    ]
    subject = models.CharField(max_length=1,choices=SUBJECT_CHOICES,blank=False)
    school_class = models.ForeignKey(Group,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        user_metadata = AllUsersMetaData.objects.filter(user=self.user).first()
        return f"{user_metadata.first_name} {user_metadata.last_name}"