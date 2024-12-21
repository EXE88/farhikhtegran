from django.db import models
from django.contrib.auth.models import User,Group
from lessons.models import *
from django.core.exceptions import ValidationError

#TODO: use Meta class and add unique to fileds remove thah lines of code from clean

class AllUsersMetaData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False , verbose_name="کاربر")
    first_name = models.CharField(max_length=50,blank=False , verbose_name="نام")
    last_name = models.CharField(max_length=50,blank=False , verbose_name="نام خانوادگی")
    age = models.PositiveSmallIntegerField(blank=False , verbose_name="سن")
    is_teacher = models.BooleanField(default=False,blank=False , verbose_name="ایا معلم است")

    def clean(self):
        if AllUsersMetaData.objects.filter(user=self.user).exclude(id=self.id).exists():
            raise ValidationError(f"این اطلاعات قبلا ثبت شده است")

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)
    
class TeachersMetaData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False , verbose_name="کاربر")
    phone_number = models.PositiveBigIntegerField(blank=False , verbose_name="شماره تلفن")
    lessons = models.ManyToManyField(Lesson,blank=False , verbose_name="درس ها")

    def clean(self):
        if TeachersMetaData.objects.filter(user=self.user).exclude(id=self.id).exists():
            raise ValidationError(f"این اطلاعات قبلا ثبت شده است")

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs) 

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
            raise ValidationError(f"این اطلاعات قبلا ثبت شده است")

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)
    
class TeacherLessonAssignment(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,blank=False , verbose_name="معلم")
    school_class = models.ForeignKey(Group,on_delete=models.CASCADE,blank=False , verbose_name="کلاس")
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,blank=False , verbose_name="درس")

    def clean(self):
        teacher_classes = User.objects.get(username=self.teacher.username).groups.all()
        if self.school_class not in teacher_classes:
            raise ValidationError("معلم مورد نظر این کلاس را بر نداشته است")
        
        teacher_lessons = TeachersMetaData.objects.get(user=self.teacher).lessons.all()
        if self.lesson not in teacher_lessons:
            raise ValidationError("معلم مورد نظر این درس را بر نداشته است")
        
        if TeacherLessonAssignment.objects.filter(teacher=self.teacher,school_class=self.school_class,lesson=self.lesson).exclude(id=self.id).exists():
            raise ValidationError(f"این اطلاعات قبلا ثبت شده است")
        
    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)