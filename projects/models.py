from django.db import models

# Create your models here.

from django.db import models

class Project(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField()
    #image = models.FilePathField(path="projects/static/img")
