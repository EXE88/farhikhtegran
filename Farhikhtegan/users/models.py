from django.db import models
from django.contrib.auth.models import User
from lessons.models import *

class UsersMetaData(models.Model):
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50,null=False)
    age = models.PositiveSmallIntegerField(null=False)
    is_teacher = models.BooleanField(default=False,null=False)
    lessons = models.ManyToManyField(Lesson)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"