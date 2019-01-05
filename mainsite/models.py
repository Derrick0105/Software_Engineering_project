from django.db import models
from django.utils import timezone
# Create your models here.
class Location_set(models.Model):
    loaction=models.CharField(max_length=20)

    def __str__(self):
        return self.loaction

class Job_list(models.Model):
    title=models.CharField(max_length=200)
    location=models.CharField(max_length=10)
    name=models.CharField(max_length=200)
    skill=models.CharField(max_length=200)
    experience=models.PositiveIntegerField()
    description=models.TextField(default='說明職務內容')
    pub_date=models.DateTimeField(default=timezone.now)
    logo=models.ImageField(default='未選擇',upload_to='photos')

    def __str__(self):
        return self.name


class User(models.Model):
    account = models.CharField(max_length=200, default='登入帳號')
    name=models.CharField(max_length=20,null=False)
    password=models.CharField(max_length=20,null=False)
    department=models.CharField(max_length=20,default='請輸入系級')
    description = models.CharField(max_length=200,default='請輸入履歷')
    email = models.EmailField()
    enabled=models.BooleanField(default=False)


    def __str__(self):
        return self.name




