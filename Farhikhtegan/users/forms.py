from django import forms
from .models import AllUsersMetaData , TeachersMetaData , StudentsMetaData , WhatEveryTeacherTeachForEachClass
from django.contrib.auth.models import User

class CustomUserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        metadata = AllUsersMetaData.objects.filter(user=obj).first()
        if metadata:
            return f"{metadata.first_name} {metadata.last_name}"
        return obj.username  

class AllUsersMetaDataForm(forms.ModelForm):
    pass

class TeachersMetaDataForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=AllUsersMetaData.objects.values_list('user', flat=True))
    class Meta:
        model = TeachersMetaData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(allusersmetadata__is_teacher=True)

class StudentsMetaDataForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=AllUsersMetaData.objects.values_list('user', flat=True))
    class Meta:
        model = StudentsMetaData
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(allusersmetadata__is_teacher=False)

class WhatEveryTeacherTeachForEachClassForm(forms.ModelForm):
    teacher = CustomUserChoiceField(queryset=AllUsersMetaData.objects.values_list('user', flat=True))
    class Meta:
        model = WhatEveryTeacherTeachForEachClass
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = User.objects.filter(allusersmetadata__is_teacher=True)