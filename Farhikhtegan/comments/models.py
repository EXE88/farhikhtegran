from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Comment(models.Model):
    from_teacher = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,related_name="comments_as_teacher")
    to_student = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,related_name="comments_as_student")
    description = models.TextField(max_length=500,blank=False)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)

    def clean(self):
        teacher_classes = self.from_teacher.groups.all()
        student_groups = self.to_student.groups.all()

        if not student_groups.intersection(teacher_classes):
            raise ValidationError("این دانش اموز در جزو دانش اموزان این معلم نیست")
    
    def save(self,*args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)