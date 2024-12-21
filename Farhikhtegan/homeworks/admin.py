from django.contrib import admin
from .models import *
from users.models import AllUsersMetaData
import jdatetime
from .forms import HomeWorkForm

@admin.register(HomeWork)
class HomeWorksAdmin(admin.ModelAdmin):
    list_display = ("teacher","lesson_name","for_class","homework_description","expirations_date_jalali","created_at_jalali","updated_at_jalali")
    form = HomeWorkForm

    def teacher(self,obj):
        teacher_details = AllUsersMetaData.objects.get(user=obj.from_teacher)
        return teacher_details.first_name + " " + teacher_details.last_name
    teacher.short_description = "نام و نام خانوادگی"

    def lesson_name(self,obj):
        return Lesson.objects.get(id=obj.for_lesson.id).name
    lesson_name.short_description = "نام درس"

    def created_at_jalali(self,obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.created_at).strftime('%Y/%m/%d')
    created_at_jalali.short_description = "تاریخ ایجاد"

    def updated_at_jalali(self,obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.updated_at).strftime('%Y/%m/%d')
    updated_at_jalali.short_description = "تاریخ ویرایش"
    
    def expirations_date_jalali(self,obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.expiration_date).strftime("%Y/%m/%d")
    expirations_date_jalali.short_description = "تاریخ اتمام مهلت"

    def homework_description(self,obj):
        if len(obj.description) > 25:
            return "... " + obj.description[:25]
        return obj.description
    homework_description.short_description = "توضیحات"