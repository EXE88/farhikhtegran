from django.contrib import admin
from .models import *
from .forms import *

@admin.register(AllUsersMetaData)
class AllUsersMetaDataAdmin(admin.ModelAdmin):
    form = AllUsersMetaDataForm

@admin.register(TeachersMetaData)
class TeachersMetaDataAdmin(admin.ModelAdmin):
    filter_horizontal = ('lessons',)  
    form = TeachersMetaDataForm
#admin.site.register(TeachersMetaData, TeachersMetaDataAdmin)    

@admin.register(StudentsMetaData)
class StudentsMetaDataAdmin(admin.ModelAdmin):
    form = StudentsMetaDataForm
#admin.site.register(StudentsMetaData, StudentsMetaDataAdmin)

@admin.register(WhatEveryTeacherTeachForEachClass)
class WhatEveryTeacherTeachForEachClassAdmin(admin.ModelAdmin):
    form = WhatEveryTeacherTeachForEachClassForm
#admin.site.register(WhatEveryTeacherTeachForEachClass,WhatEveryTeacherTeachForEachClassAdmin)