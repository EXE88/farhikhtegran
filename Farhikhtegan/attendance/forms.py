from django import forms
from .models import *
from users.models import AllUsersMetaData
from lessons.models import Lesson

class CustomUserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        metadata = AllUsersMetaData.objects.filter(user=obj).first()
        if metadata:
            return f"{metadata.first_name} {metadata.last_name}"
        return obj.username

class StudentAttendanceForm(forms.ModelForm):
    from_teacher = CustomUserChoiceField(queryset=AllUsersMetaData.objects.values_list('user', flat=True))
    to_student = CustomUserChoiceField(queryset=AllUsersMetaData.objects.values_list('user', flat=True))
    class Meta:
        model = StudentAttendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['from_teacher'].queryset = User.objects.filter(allusersmetadata__is_teacher=True)
        self.fields['to_student'].queryset = User.objects.filter(allusersmetadata__is_teacher=False)