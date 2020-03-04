from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now=True ,max_length=30)
    def __str__(self):
        return self.category_name


class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.content
    
class Technology(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    img_url = models.CharField(max_length=500,default='null')
    content_url = models.CharField(max_length=100,default='null')
    summary = models.CharField(max_length=500,default='null')
    image = models.ImageField(upload_to='uploads',default='null')
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Business(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    img_url = models.CharField(max_length=500,default='null')
    content_url = models.CharField(max_length=100,default='null')
    summary = models.CharField(max_length=500,default='null')
    image = models.ImageField(upload_to='uploads/',default='null')
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Political(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    img_url = models.CharField(max_length=500,default='null')
    content_url = models.CharField(max_length=100,default='null')
    summary = models.CharField(max_length=500,default='null')
    image = models.ImageField(upload_to='uploads/',default='null')
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title




class extendeduser(models.Model):
    user_can_post = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


