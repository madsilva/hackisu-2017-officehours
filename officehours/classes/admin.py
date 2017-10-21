from django.contrib import admin

from .models import Course, Student, Session, Question

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Session)
admin.site.register(Question)