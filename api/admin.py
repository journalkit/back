from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Discipline)
admin.site.register(Theme)
admin.site.register(Group)
admin.site.register(Statement)
admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(Record)
admin.site.register(Exam)
admin.site.register(ExamList)
