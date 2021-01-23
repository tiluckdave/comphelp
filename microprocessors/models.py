from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=130)
    mainImage = models.ImageField(upload_to="images/data-structures")
    title = models.CharField(max_length=200)
    short = models.TextField(max_length=300)
    intro = models.TextField()
    explain = models.TextField()
    image1 = models.ImageField(upload_to="images/data-structures")
    image2 = models.ImageField(upload_to="images/data-structures")
    code = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class MpPostComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return "New comment By - " + self.user.username 

class Note(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    short = models.TextField(max_length=300)
    file = models.FileField(upload_to='notes/microprocessors')
    date = models.DateField()

    def __str__(self):
        return self.title

class Mcq(models.Model):
    sno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.question

class Link(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    short = models.TextField(max_length=200)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title