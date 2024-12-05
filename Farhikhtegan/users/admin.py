from django.contrib import admin
from .models import *
from .forms import *

admin.site.register(AllUsersMetaData)

class TeachersMetaDataAdmin(admin.ModelAdmin):
    filter_horizontal = ('lessons',)  
    form = TeachersMetaDataForm
admin.site.register(TeachersMetaData, TeachersMetaDataAdmin)    

class StudentsMetaDataAdmin(admin.ModelAdmin):
    form = StudentsMetaDataForm
admin.site.register(StudentsMetaData, StudentsMetaDataAdmin)