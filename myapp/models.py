

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __int__(self):
        return self.email

class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __int__(self):
        return self.name

class Blogpost(models.Model):
    tittle=models.CharField(max_length=50)
    content=models.TextField()
    puplished_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)

    def __int__(self):
        return self.tittle



class Item(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __int__(self):
        return self.name

