from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):# nó giống như cái lớp đc tạo từ lớp trừu tượng
    avatar = models.ImageField(upload_to='uploads/%Y/%m')
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,null=False,unique=True)

class ItemBase(models.Model):
    class Meta:
        abstract = True # la mot model truu tuong trong opp là để nó không tạo ra table ItemBase trong database
    subject = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='courses/%Y/%M',default=None)# chỗ này MEDIA_ROOT + upload_to
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Course(ItemBase):
    class Meta:
        unique_together = ('subject','category') # trong 1 category ko đc phép trùng tên subject
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)# de thoa man nhat quan du lieu

    def __str__(self):
        return self.subject

class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject','course') # trong 1 course ko đc trùng subject
    content = models.TextField()
    course = models.ForeignKey(Course,related_name="lessons",on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag',blank= True,null= True)# thì những cái đã có trc mà chưa thiết lập cho cái này thì nó sẽ là null hoặc none

    def __str__(self):
        return self.subject


class Tag(models.Model):
    name = models.CharField(max_length=50, unique= True)


    def __str__(self):
        return self.name
