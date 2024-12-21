from django.db import models
from django.contrib.auth.models import User
from users.models import AllUsersMetaData , TeachersMetaData
from lessons.models import Lesson
import jdatetime
from django.core.exceptions import ValidationError
from django.utils import timezone

#TODO:return back created_at_jalali , updated_at_jajli inside of the models in the admin file didnt work

class StudentAttendance(models.Model):
    from_teacher = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,related_name="student_attendancea_as_from_teacher",verbose_name="از طرف معلم")
    to_student = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,related_name="student_attendancea_as_to_student",verbose_name="به دانش اموز")
    in_lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,blank=False,verbose_name="در کلاس")
    is_present = models.BooleanField(default=False,blank=False,verbose_name="وضعیت حضور")
    created_at = models.DateTimeField(auto_now_add=True,blank=False,verbose_name="ثبت شده در تاریخ")
    updated_at = models.DateTimeField(auto_now=True,blank=False,verbose_name="اپدیت شده در تاریخ")
    
    def __str__(self):
        if self.is_present:
            present = "حاضر"
        else:
            present = "غایب"

        student_first_name = AllUsersMetaData.objects.get(user=self.to_student).first_name
        student_last_name = AllUsersMetaData.objects.get(user=self.to_student).last_name

        return f"{student_first_name} {student_last_name}"
    
    def clean(self):
        teacher_classes = self.from_teacher.groups.all()
        student_groups = self.to_student.groups.all()

        if not student_groups.intersection(teacher_classes):
            raise ValidationError("این دانش اموز در جزو دانش اموزان این معلم نیست")
        
        if self.in_lesson not in TeachersMetaData.objects.get(user=self.from_teacher).lessons.all():
            raise ValidationError("معلم این درس را بر نداشته است")

        today = timezone.now().date()
        if StudentAttendance.objects.filter(
            from_teacher=self.from_teacher,
            to_student=self.to_student,
            in_lesson=self.in_lesson,
            created_at__date=today
        ).exclude(id=self.id).exists():
            raise ValidationError(" معلم مورد نظر برای این دانش آموز در این درس در امروز حضور/غیاب ثبت کرده است")
        
    def save(self,*args,**kwargs):
        self.clean()
        return super().save(*args, **kwargs)