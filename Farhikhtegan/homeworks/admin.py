from django.contrib import admin
from django.forms import TextInput, Textarea
from .models import *
from .forms import HomeWorkForm

class HomeWorksAdmin(admin.ModelAdmin):
    form = HomeWorkForm
admin.site.register(HomeWork,HomeWorksAdmin)
