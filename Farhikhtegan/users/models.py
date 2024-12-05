from django.db import models
from django.contrib.auth.models import User
from lessons.models import *

class AllUsersMetaData(models.Model):
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE,blank=False)
    first_name = models.CharField(max_length=50,null=False,blank=False)
    last_name = models.CharField(max_length=50,null=False,blank=False)
    age = models.PositiveSmallIntegerField(null=False,blank=False)
    is_teacher = models.BooleanField(default=False,null=False,blank=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class TeachersMetaData(models.Model):
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE,blank=False)
    lessons = models.ManyToManyField(Lesson,blank=False)
    def __str__(self):
        user_metadata = AllUsersMetaData.objects.filter(user=self.user).first()
        return f"{user_metadata.first_name} {user_metadata.last_name}"

class StudentsMetaData(models.Model):
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE,blank=False)
    SUBJECT_CHOICES = [
        ('1', 'تجربی'),
        ('2', 'ریاضی'),
        ('3', 'انسانی'),
    ]
    subject = models.CharField(max_length=1,choices=SUBJECT_CHOICES,blank=False,null=False)
    def __str__(self):
        user_metadata = AllUsersMetaData.objects.filter(user=self.user).first()
        return f"{user_metadata.first_name} {user_metadata.last_name}"