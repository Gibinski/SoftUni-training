from django.db import models

# Create your models here.

class Tasks(models.Model):
    # varcha
    title = models.CharField(max_length=30, null=False)
    # text
    description = models.TextField(max_length=130)
    # int
    priority = models.IntegerField(default=1)