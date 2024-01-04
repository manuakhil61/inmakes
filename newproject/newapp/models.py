from django.db import models

# Create your models here.
class pics(models.Model):
    name=models.CharField(max_length=150)
    image=models.ImageField(upload_to='pics')
    descr=models.TextField()

    def __str__(self):
         return self.name