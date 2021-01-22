from django.db import models

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    short = models.TextField(max_length=300)
    content = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title