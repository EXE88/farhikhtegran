from django.contrib import admin
from .models import *

class UsersMetaDataAdmin(admin.ModelAdmin):
    filter_horizontal = ('lessons',)

admin.site.register(UsersMetaData , UsersMetaDataAdmin)
