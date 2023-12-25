from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin
# Register your models here.
# admin.site.register(CustomUser)


class UserModel(UserAdmin):
    list_display=['username','user_type']
    
admin.site.register(CustomUser,UserModel)

admin.site.register(Acad_year)
admin.site.register(Branch)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)