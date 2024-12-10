from django.contrib import admin
from .models import *
from .forms import *

class StudentAttendanceAdmin(admin.ModelAdmin):
    form = StudentAttendanceForm
    readonly_fields = ('created_at_jalali','updated_at_jalali')
    
    def created_at_jalali(self, obj):
        return obj.created_at_jalali()
    created_at_jalali.short_description = "ایجاد شده در تاریخ"

    def updated_at_jalali(self, obj):
        return obj.updated_at_jalali()
    updated_at_jalali.short_description = "ویرایش شده در تاریخ"

admin.site.register(StudentAttendance,StudentAttendanceAdmin)