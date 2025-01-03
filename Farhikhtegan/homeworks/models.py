from django.db import models
from django.contrib.auth.models import User , Group
from lessons.models import Lesson
from users.models import TeacherLessonAssignment
from django.core.exceptions import ValidationError

class HomeWork(models.Model):
    from_teacher = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,verbose_name="از طرف معلم")
    for_lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,blank=False,verbose_name="برای درس")
    for_class = models.ForeignKey(Group,on_delete=models.CASCADE,blank=False,verbose_name="برای کلاس")
    description = models.TextField(max_length=500,blank=False,verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True,blank=False,verbose_name="ایجاد شده در تاریخ")
    updated_at = models.DateTimeField(auto_now=True,blank=False,verbose_name="اپدیت شده در تاریخ")
    expiration_date = models.DateField(blank=False,verbose_name="مهلت اتمام")

    def __str__(self):
        class_name = self.for_class.name
        lesson = self.for_lesson.name
        return f"{class_name}-{lesson}"
    
    def clean(self):
        if not TeacherLessonAssignment.objects.filter(
            teacher=self.from_teacher, 
            school_class=self.for_class, 
            lesson=self.for_lesson
        ).exists():
            raise ValidationError("این معلم نمیتواند به این کلاس یا در این درس تکلیف بدهد")

    def save(self,*args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)