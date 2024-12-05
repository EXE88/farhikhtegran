from django import forms
from .models import TeachersMetaData, AllUsersMetaData , StudentsMetaData
from django.contrib.auth.models import User

class TeachersMetaDataForm(forms.ModelForm):
    class Meta:
        model = TeachersMetaData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(allusersmetadata__is_teacher=True)

class StudentsMetaDataForm(forms.ModelForm):
    class Meta:
        model = StudentsMetaData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(allusersmetadata__is_teacher=False)