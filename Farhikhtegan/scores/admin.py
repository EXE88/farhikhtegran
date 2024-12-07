from django.contrib import admin
from .models import *
from .forms import *

#TODO:add verbos names
class CreateStudentsScoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at_jalali','updated_at_jalali')
    form = CreateStudentsScoreForm
admin.site.register(CreateStudentScore, CreateStudentsScoreAdmin)