from django.db import models

# Create your models here.

class Request(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return 'New Topic request from - ' + self.name