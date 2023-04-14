from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

# Create your models here.

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name



class Pain(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)

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
    image = models.ImageField(upload_to='yoga/images/',blank=True)
    video = models.CharField(max_length=1000,blank=True)
    Disease=models.ManyToManyField(Disease, blank=True)
    Pain=models.ManyToManyField(Pain,blank=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.name




