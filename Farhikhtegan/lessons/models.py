from django.db import models
from django.core.exceptions import ValidationError

class Lesson(models.Model):
    name = models.CharField(max_length=50 , blank=False , verbose_name="نام درس")

    def __str__(self):
        return self.name
    
    def clean(self):
        if Lesson.objects.filter(name=self.name).exclude(id=self.id).exists():
            raise ValidationError(f"این اطلاعات قبلا ثبت شده است")

    def save(self, *args, **kwargs):
        self.clean() 
        super().save(*args, **kwargs)