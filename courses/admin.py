from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget # neu dung ckeditor thi no chi co in dam in nghieng,... don gian thoi
from courses.models import Course,Category,User,Lesson
# Register your models here.


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = "__all__"


class LessonTagInline(admin.TabularInline):
    model = Lesson.tags.through# through de dinh nghia model trung gian


class Lesson_Admin(admin.ModelAdmin):

    class Media:
        css = {'all': ('/static/css/main.css',)}  # pphải có dấu , vì nó là tupe

    form = LessonForm
    list_display = ["id","subject","active","create_date","course"]
    search_fields = ["subject","create_date","course__subject"]
    list_filter = ["subject","course__subject"]
    readonly_fields = ["avatar"]
    inlines = (LessonTagInline, )

    def avatar(self,lesson):# thêm ảnh vào trong và chỉ có thể xem
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120px' />".format(img_url=lesson.image.name,alt=lesson.subject))




class LessonInlineAdmin(admin.StackedInline): #inline la ta nhung mot cai form khac vao
    model = Lesson #ke thua model
    pk_name = 'course'

class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInlineAdmin,) #no phai la tupe

admin.site.register(User)
admin.site.register(Course,CourseAdmin)
admin.site.register(Category)
admin.site.register(Lesson,Lesson_Admin)