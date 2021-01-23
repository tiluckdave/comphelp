from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=130)
    mainImage = models.ImageField(upload_to="images/computer-graphics")
    title = models.CharField(max_length=200)
    short = models.TextField(max_length=300)
    intro = models.TextField()
    explain = models.TextField()
    image1 = models.ImageField(upload_to="images/computer-graphics")
    image2 = models.ImageField(upload_to="images/computer-graphics")
    algo = models.TextField()
    code = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class Note(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    short = models.TextField(max_length=300)
    file = models.FileField(upload_to='notes/computer-graphics')
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