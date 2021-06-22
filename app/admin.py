from django.contrib import admin
from . models import Student

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','age']
    

admin.site.register(Student,studentAdmin)