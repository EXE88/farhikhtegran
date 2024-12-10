from django import forms
from .models import *
from users.models import AllUsersMetaData
from lessons.models import Lesson

class StudentAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['from_teacher'].queryset = User.objects.filter(allusersmetadata__is_teacher=True)
        self.fields['to_student'].queryset = User.objects.filter(allusersmetadata__is_teacher=False)