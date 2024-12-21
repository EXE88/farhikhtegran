from django.contrib import admin
from .models import *

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("name",)