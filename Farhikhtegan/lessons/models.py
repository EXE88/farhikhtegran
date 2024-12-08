from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=50 , blank=False , verbose_name="نام درس")

    def __str__(self):
        return self.name
