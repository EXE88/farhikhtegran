from django.contrib import admin
from .models import *
from .forms import *
from django.contrib import messages

@admin.register(AllUsersMetaData)
class AllUsersMetaDataAdmin(admin.ModelAdmin):
    list_display = ('user','first_name','last_name','age','is_teacher')
    search_fields = ("first_name","last_name")
    list_filter = ("is_teacher",)
    form = AllUsersMetaDataForm

@admin.register(TeachersMetaData)
class TeachersMetaDataAdmin(admin.ModelAdmin):
    filter_horizontal = ('lessons',)
    list_display = ("teacher","phone_number","list_of_lessons","list_of_classes")  
    search_fields = ('id',)
    list_filter = ("lessons","user__groups")
    form = TeachersMetaDataForm

    def teacher(self,obj):
        teacher_details = AllUsersMetaData.objects.get(user=obj.user)
        return teacher_details.first_name + " " + teacher_details.last_name
    teacher.short_description = "نام و نام خانوادگی"

    def list_of_lessons(self, obj):
        return " , ".join([lesson.name for lesson in obj.lessons.all()])
    list_of_lessons.short_description = "درس‌ ها"

    def list_of_classes(self, obj):
        return " , ".join([group.name for group in obj.user.groups.all()])
    list_of_classes.short_description = "کلاس ها"

    def get_search_results(self, request, queryset, search_term):
        if search_term:
            queryset = queryset.filter(user__allusersmetadata__first_name__icontains=search_term) | queryset.filter(user__allusersmetadata__last_name__icontains=search_term)
        return queryset, False

@admin.register(StudentsMetaData)
class StudentsMetaDataAdmin(admin.ModelAdmin):
    list_display = ("student","address","father_phone_number","mother_phone_number","home_phone_number","grade","subject")
    search_fields = ('id',)
    list_filter = ("grade","subject")
    form = StudentsMetaDataForm

    def get_search_results(self, request, queryset, search_term):
        if search_term:
            queryset = queryset.filter(user__allusersmetadata__first_name__icontains=search_term) | queryset.filter(user__allusersmetadata__last_name__icontains=search_term)
        return queryset, False

    def student(self,obj):
        student_details = AllUsersMetaData.objects.get(user=obj.user)
        return student_details.first_name + " " + student_details.last_name
    student.short_description = "نام و نام خانوادگی"

@admin.register(TeacherLessonAssignment)
class TeacherLessonAssignmentAdmin(admin.ModelAdmin):
    list_display = ("teacher_name_and_family","school_class","lesson")
    form = TeacherLessonAssignmentForm

    def teacher_name_and_family(self,obj):
        teacher_details = AllUsersMetaData.objects.get(user=obj.teacher)
        return teacher_details.first_name + " " + teacher_details.last_name
    teacher_name_and_family.short_description = "نام و نام خانوادگی"
