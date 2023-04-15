from django.db import models


class Profile(models.Model):
    display_name = models.CharField(max_length=30)
    mobile = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    dob = models.DateField()
    photo=models.FileField(upload_to='profile/',null=True,blank=True)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Hobby(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='user_hobby',null=True,blank=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
