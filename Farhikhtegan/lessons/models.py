from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=50 , null=False , blank=False)

    def __str__(self):
        return self.name
