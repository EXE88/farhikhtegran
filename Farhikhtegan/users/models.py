from django.db import models
from django.contrib.auth.models import User,Group
from lessons.models import *
from django.core.exceptions import ValidationError

class AllUsersMetaData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False , verbose_name="کاربر")
    first_name = models.CharField(max_length=50,blank=False , verbose_name="نام")
    last_name = models.CharField(max_length=50,blank=False , verbose_name="نام خانوادگی")
    age = models.PositiveSmallIntegerField(blank=False , verbose_name="سن")
    is_teacher = models.BooleanField(default=False,blank=False , verbose_name="ایا معلم است")

    def clean(self):
        if AllUsersMetaData.objects.filter(user=self.user).exclude(id=self.id).exists():
            raise ValidationError(f"اطلاعات برای این کاربر ({self.user}) قبلاً ثبت شده است.")

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class TeachersMetaData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False , verbose_name="کاربر")
    phone_number = models.PositiveBigIntegerField(blank=False , verbose_name="شماره تلفن")
    lessons = models.ManyToManyField(Lesson,blank=False , verbose_name="درس ها")

    def clean(self):
        if TeachersMetaData.objects.filter(user=self.user).exclude(id=self.id).exists():
            raise ValidationError(f"اطلاعات برای این کاربر ({self.user}) قبلاً ثبت شده است.")

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)

    def __str__(self):
        user_metadata = AllUsersMetaData.objects.filter(user=self.user).first()
        return f"{user_metadata.first_name} {user_metadata.last_name}"

class StudentsMetaData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False , verbose_name="دانش اموز")
    address = models.CharField(max_length=300,blank=False , verbose_name="ادرس خانه")
    father_phone_number = models.PositiveBigIntegerField(blank=False , verbose_name="شماره تلفن پدر")
    mother_phone_number = models.PositiveBigIntegerField(blank=False , verbose_name="شماره تلفن مادر")
    home_phone_number = models.PositiveBigIntegerField(blank=False , verbose_name="شماره تلفن خانه")
    GRADE_CHOICES = [
        ('1', 'دهم'),
        ('2', 'یازدهم '),
        ('3', 'دوازدهم'),        
    ]
    grade = models.CharField(max_length=1,choices=GRADE_CHOICES,blank=False , verbose_name="پایه")
    SUBJECT_CHOICES = [
        ('1', 'تجربی'),
        ('2', 'ریاضی'),
        ('3', 'انسانی'),
    ]
    subject = models.CharField(max_length=1,choices=SUBJECT_CHOICES,blank=False , verbose_name="رشته")

    def clean(self):
        if StudentsMetaData.objects.filter(user=self.user).exclude(id=self.id).exists():
            raise ValidationError(f"اطلاعات برای این کاربر ({self.user}) قبلاً ثبت شده است.")

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)

    def __str__(self):
        user_metadata = AllUsersMetaData.objects.filter(user=self.user).first()
        return f"{user_metadata.first_name} {user_metadata.last_name}"
    
class WhatEveryTeacherTeachForEachClass(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,blank=False , verbose_name="معلم")
    school_class = models.ForeignKey(Group,on_delete=models.CASCADE,blank=False , verbose_name="کلاس")
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,blank=False , verbose_name="درس")

    def clean(self):
        if WhatEveryTeacherTeachForEachClass.objects.filter(teacher=self.teacher,school_class=self.school_class,lesson=self.lesson).exclude(id=self.id).exists():
            raise ValidationError(f"اطلاعات برای این کاربر ({self.teacher}) قبلاً ثبت شده است.")

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)

    def __str__(self):
        teacher_fullname = AllUsersMetaData.objects.get(user=self.teacher)
        return f"{teacher_fullname.first_name} {teacher_fullname.last_name}-{self.school_class.name}-{self.lesson.name}"