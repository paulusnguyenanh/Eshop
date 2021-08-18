from django.contrib import admin
from courses.models import Course,Category,User,Lesson
# Register your models here.

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson)