from django.contrib import admin
from .models import *
from .forms import *

@admin.register(CreateStudentScore)
class CreateStudentsScoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at_jalali','updated_at_jalali')
    list_display = ('teacher','student','lesson','score','created_at_jalali','updated_at_jalali')
    search_fields = ('id',)
    list_filter = ("lesson","created_at")
    form = CreateStudentsScoreForm

    def created_at_jalali(self,obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.created_at).strftime('%Y/%m/%d')
    created_at_jalali.short_description = "تاریخ ایجاد"

    def updated_at_jalali(self,obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.updated_at).strftime('%Y/%m/%d')
    updated_at_jalali.short_description = "تاریخ ویرایش"
    
    def teacher(self,obj):
        teacher_details = AllUsersMetaData.objects.get(user=obj.from_teacher)
        return teacher_details.first_name + " " + teacher_details.last_name
    teacher.short_description = "از طرف معلم"
    
    def student(self,obj):
        student_details = AllUsersMetaData.objects.get(user=obj.to_student)
        return student_details.first_name + " " + student_details.last_name
    student.short_description = "به دانش اموز"

    def get_search_results(self, request, queryset, search_term):
        if search_term:
            queryset = queryset.filter(from_teacher__allusersmetadata__first_name__icontains=search_term) | queryset.filter(from_teacher__allusersmetadata__last_name__icontains=search_term) | queryset.filter(to_student__allusersmetadata__first_name__icontains=search_term) | queryset.filter(to_student__allusersmetadata__last_name__icontains=search_term) | queryset.filter(lesson__name__icontains=search_term)
        return queryset, False