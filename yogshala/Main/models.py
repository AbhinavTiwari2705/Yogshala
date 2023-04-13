from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class Pain(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.IntegerField()

    def __str__(self):
        return self.name




class User(User):
    # name = models.CharField(max_length=100)
    # email = models.EmailField()
    # password = models.CharField(max_length=100)
    # phone = models.CharField(max_length=100)
    Disease=models.ManyToManyField(Disease)
    Pain=models.ManyToManyField(Pain)

    def __str__(self):
        return self.name



class yoga(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='yoga/images/')
    video = models.CharField(max_length=1000)
    Disease=models.ManyToManyField(Disease)
    Pain=models.ManyToManyField(Pain)

    def __str__(self):
        return self.name




