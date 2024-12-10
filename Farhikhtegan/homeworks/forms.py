from django import forms
from .models import *
from django.contrib.auth.models import User
from users.models import AllUsersMetaData

class HomeWorkForm(forms.ModelForm):
    class Meta:
        model = HomeWork
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['from_teacher'].queryset = User.objects.filter(allusersmetadata__is_teacher=True)