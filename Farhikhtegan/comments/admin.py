from django.contrib import admin
from .models import Comment
import jdatetime
from users.models import AllUsersMetaData
from .forms import CommentForm

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentForm
    list_display = ("teacher","student","comment_discription","created_at_jalali","updated_at_jalali")
    readonly_fields = ("created_at_jalali","updated_at_jalali")

    def teacher(self,obj):
        teacher_details = AllUsersMetaData.objects.get(user=obj.from_teacher)
        return teacher_details.first_name + " " + teacher_details.last_name
    teacher.short_description = "از طرف معلم"

    def student(self,obj):
        student_details = AllUsersMetaData.objects.get(user=obj.to_student)
        return student_details.first_name + " " + student_details.last_name
    student.short_description = "به دانش اموز"

    def comment_discription(self,obj):
        if len(obj.description) > 25:
            return "... " + obj.description[:25]
        return obj.description
    comment_discription.short_description = "توضیحات"

    def created_at_jalali(self,obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.created_at).strftime('%Y/%m/%d')
    created_at_jalali.short_description = "تاریخ ایجاد"

    def updated_at_jalali(self,obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.updated_at).strftime('%Y/%m/%d')
    updated_at_jalali.short_description = "تاریخ ویرایش"
