from django.db import models
from django.contrib.auth.models import User
from lessons.models import Lesson
from django.core.validators import MinValueValidator , MaxValueValidator
import jdatetime
from users.models import AllUsersMetaData

#TODO:add fardsi verbos names
class CreateStudentScore(models.Model):
    from_teacher = models.ForeignKey(User,blank=False,on_delete=models.CASCADE,related_name="students_score_as_from_teacher")
    to_student = models.ForeignKey(User,blank=False,on_delete=models.CASCADE,related_name="students_score_as_to_student")
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)
    lesson = models.ForeignKey(Lesson,blank=False,on_delete=models.CASCADE)
    score = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(20)],blank=False)

    def created_at_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.created_at).strftime('%Y/%m/%d')

    def updated_at_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.updated_at).strftime('%Y/%m/%d')
    
    def __str__(self):
        teacher = AllUsersMetaData.objects.get(user=self.from_teacher)
        student = AllUsersMetaData.objects.get(user=self.to_student)
        
        return f"{teacher.first_name} {teacher.last_name}-{student.first_name} {student.last_name}-{self.lesson.name}"