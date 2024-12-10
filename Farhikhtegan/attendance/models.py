from django.db import models
from django.contrib.auth.models import User
from users.models import AllUsersMetaData
from lessons.models import Lesson
import jdatetime

class StudentAttendance(models.Model):
    from_teacher = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,related_name="student_attendancea_as_from_teacher",verbose_name="از طرف معلم")
    to_student = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,related_name="student_attendancea_as_to_student",verbose_name="به دانش اموز")
    in_lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,blank=False,verbose_name="در کلاس")
    is_present = models.BooleanField(default=False,blank=False,verbose_name="وضعیت حضور")
    created_at = models.DateTimeField(auto_now_add=True,blank=False,verbose_name="ثبت شده در تاریخ")
    updated_at = models.DateTimeField(auto_now=True,blank=False,verbose_name="اپدیت شده در تاریخ")

    def created_at_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.created_at).strftime('%Y/%m/%d')

    def updated_at_jalali(self):
        return jdatetime.datetime.fromgregorian(datetime=self.updated_at).strftime('%Y/%m/%d')
    
    def __str__(self):
        if self.is_present:
            present = "حاضر"
        else:
            present = "غایب"

        student_first_name = AllUsersMetaData.objects.get(user=self.to_student).first_name
        student_last_name = AllUsersMetaData.objects.get(user=self.to_student).last_name

        return f"{student_first_name} {student_last_name}-{self.created_at_jalali()}-{present}"