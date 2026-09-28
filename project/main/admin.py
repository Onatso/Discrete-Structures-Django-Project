from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Task)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Achievement)
admin.site.register(UserAchievement)
admin.site.register(UserTask)
admin.site.register(Comment)