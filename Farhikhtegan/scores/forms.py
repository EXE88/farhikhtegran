from django import forms
from django.contrib.auth.models import User
from .models import *
from users.models import AllUsersMetaData

class CreateStudentsScoreForm(forms.ModelForm):
    class Meta:
        model = CreateStudentScore
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['from_teacher'].queryset = User.objects.filter(allusersmetadata__is_teacher=True)
        self.fields['to_student'].queryset = User.objects.filter(allusersmetadata__is_teacher=False)