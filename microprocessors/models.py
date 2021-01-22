from django.db import models

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