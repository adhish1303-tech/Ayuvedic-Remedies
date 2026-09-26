from django.db import models

# Create your models here.
class login_cred(models.Model):
    email = models.EmailField()
    password = models.TextField()

class Register(models.Model):
    Name = models.TextField()
    Email = models.EmailField()
    Contact = models.IntegerField()
    Password = models.TextField()

class admin(models.Model):
    email = models.EmailField()
    password = models.TextField()

class remedies(models.Model):
    user_name = models.TextField()
    user_email = models.EmailField()
    Name = models.TextField()
    Issues = models.TextField()
    Solution = models.TextField()
    img = models.FileField(upload_to = "images/")   
    video = models.FileField(upload_to = "videos/")
    Benefits = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=50, default='PENDING')
