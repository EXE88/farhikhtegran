from django import forms
from .models import *
from django.contrib.auth.models import User
from users.models import AllUsersMetaData

class CustomUserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        metadata = AllUsersMetaData.objects.filter(user=obj).first()
        if metadata:
            return f"{metadata.first_name} {metadata.last_name}"
        return obj.username 

class HomeWorkForm(forms.ModelForm):
    from_teacher = CustomUserChoiceField(queryset=AllUsersMetaData.objects.values_list('user', flat=True))
    class Meta:
        model = HomeWork
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['from_teacher'].queryset = User.objects.filter(allusersmetadata__is_teacher=True)