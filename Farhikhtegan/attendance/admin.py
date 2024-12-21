from django.contrib import admin
from .models import *
from .forms import *
import jdatetime

@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    form = StudentAttendanceForm
    readonly_fields = ('created_at_jalali','updated_at_jalali')
    list_display = ("teacher",'student',"in_lesson","is_present",'created_at_jalali', 'updated_at_jalali')
    #list_filter = ('created_at_jalali', 'updated_at_jalali')

    def created_at_jalali(self,obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.created_at).strftime('%Y/%m/%d')
    created_at_jalali.short_description = "ایجاد شده در تاریخ"

    def updated_at_jalali(self,obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.updated_at).strftime('%Y/%m/%d')
    updated_at_jalali.short_description = "ویرایش شده در تاریخ"

    def teacher(self,obj):
        details = AllUsersMetaData.objects.get(user=obj.from_teacher)
        return details.first_name + " " + details.last_name
    teacher.short_description = "توسط معلم"
    def student(self, obj):
        details = AllUsersMetaData.objects.get(user=obj.to_student)
        return details.first_name + " " + details.last_name
    student.short_description = "به دانش اموز"