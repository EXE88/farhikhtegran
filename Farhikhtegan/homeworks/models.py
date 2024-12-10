from django.db import models
from django.contrib.auth.models import User , Group
from lessons.models import Lesson

class HomeWork(models.Model):
    from_teacher = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,verbose_name="از طرف معلم")
    for_lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,blank=False,verbose_name="برای کلاس")
    for_class = models.ForeignKey(Group,on_delete=models.CASCADE,blank=False,verbose_name="برای درس")
    description = models.TextField(max_length=500,blank=False,verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True,blank=False,verbose_name="ایجاد شده در تاریخ")
    updated_at = models.DateTimeField(auto_now=True,blank=False,verbose_name="اپدیت شده در تاریخ")
    expiration_date = models.DateField(blank=False,verbose_name="مهلت اتمام")