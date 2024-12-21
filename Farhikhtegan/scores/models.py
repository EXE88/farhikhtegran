from django.db import models
from django.contrib.auth.models import User
from lessons.models import Lesson
from django.core.validators import MinValueValidator , MaxValueValidator
import jdatetime
from users.models import AllUsersMetaData
from django.core.exceptions import ValidationError
from users.models import *

class CreateStudentScore(models.Model):
    from_teacher = models.ForeignKey(User,blank=False,on_delete=models.CASCADE,related_name="students_score_as_from_teacher",verbose_name="از طرف معلم")
    to_student = models.ForeignKey(User,blank=False,on_delete=models.CASCADE,related_name="students_score_as_to_student",verbose_name="به دانش اموز")
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)
    lesson = models.ForeignKey(Lesson,blank=False,on_delete=models.CASCADE,verbose_name="درس")
    score = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(20)],blank=False,verbose_name="نمره")

    def clean(self):
        teacher_classes = self.from_teacher.groups.all()
        student_groups = self.to_student.groups.all()

        if not student_groups.intersection(teacher_classes):
            raise ValidationError("این دانش اموز در جزو دانش اموزان این معلم نیست")

        student_group = self.to_student.groups.first()
        teacher_lesson_assignment_exists = TeacherLessonAssignment.objects.filter(
            teacher=self.from_teacher, 
            school_class=student_group, 
            lesson=self.lesson
        ).exists()
        
        if not teacher_lesson_assignment_exists:
            raise ValidationError("این معلم نمیتواند به این دانش اموزش در این درس نمره بدهد")

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)