from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    year = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.name