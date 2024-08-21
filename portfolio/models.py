from django.db import models

class Expertise(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title

class Gallery(models.Model):
    image = models.ImageField() 

    def __str__(self):
        return "Image Gallery"