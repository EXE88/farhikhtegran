from django.contrib import admin
from .models import *
from .forms import *

class CreateStudentsScoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at_jalali','updated_at_jalali')
    form = CreateStudentsScoreForm

    def created_at_jalali(self, obj):
        return obj.created_at_jalali()
    created_at_jalali.short_description = "ایجاد شده در تاریخ"

    def updated_at_jalali(self, obj):
        return obj.updated_at_jalali()
    updated_at_jalali.short_description = "ویرایش شده در تاریخ"

admin.site.register(CreateStudentScore, CreateStudentsScoreAdmin)