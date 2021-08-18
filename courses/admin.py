from django.contrib import admin
from django.utils.safestring import mark_safe

from courses.models import Course,Category,User,Lesson
# Register your models here.
class Lesson_Admin(admin.ModelAdmin):
    #list_display = ["id","subject","active","create_date","course"]
    search_fields = ["subject","create_date","course__subject"]
    list_filter = ["subject","course__subject"]
    readonly_fields = ["avatar"]

    def avatar(self,lesson):# thêm ảnh vào trong và chỉ có thể xem
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120px' />".format(img_url=lesson.image.name,alt=lesson.subject))

    class Media:
        css = {'all' : ('/static/css/main.css',)} # pphải có dấu , vì nó là tupe


admin.site.register(User)
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson,Lesson_Admin)